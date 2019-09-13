import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.db.models import Sum

from schools.mixins import TeacherRequiredMixin, StudentRequiredMixin
from teachers.decorators import teacher_required
from schools.models import AcademicYear
from students.models import Student
from classroom.models import Subject, ClassRoom
from .forms import ExamForm
from .models import Exam, SubjectMarkConf, Marks

@login_required
@teacher_required
def exam_view(request):
    
    # queryset = Classes.objects.filter(school = request.user.school).values('name').distinct()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.school = request.user.school
            exam.academicyear = AcademicYear.objects.get(status = True)
            exam.save()
            messages.success(request, 'Exam saved with success!')

            return redirect('exams:exams')
    else:
        # classroom = ClassRoom(school = request.user.school)
        form = ExamForm()

    exams = Exam.objects.filter(school = request.user.school)
    return render(request,"exams/exams.html", {'form': form, 'exams':exams })


class MarkEntry(TeacherRequiredMixin, View):
    def get(self, request):
        school = request.user.school
        resp ={
            'subjects': Subject.objects.filter(school=school).order_by('name'),
            'exams' : Exam.objects.filter(school=school).order_by('name'),
        }        
        return render(request,'exams/markentry.html', resp)

    def post(self,request):
        school = request.user.school
        exam = Exam.objects.get(school=school, id=request.POST['exam'])
        subject = request.POST['subject']
        if not exam.is_grade:
            if (request.POST.get('max_mark','') == '') or (request.POST.get('pass_mark','') == ''):
                return HttpResponse('Max Mark and Pass Mark is required.')

        marks = []
        marks_update = []
        for row in json.loads(request.POST['data']):
            if any(row):
                markgrade = row[2]
                if markgrade:
                    student = get_user_model().objects.get(id =row[0]).student
                    is_update = Marks.objects.filter(exam=exam,subject=subject,student = student)
                    if (is_update):
                        mark = is_update[0]
                    else:                        
                        mark = Marks(exam=exam, subject_id=subject, student = student)

                    if exam.is_grade:
                        mark.grade = markgrade.capitalize()
                    else:
                        if not markgrade.isdigit():
                            return HttpResponse('Please provide mark as Interger.')
                        if int(markgrade) > int(request.POST['max_mark']):
                            return HttpResponse('Error: Student mark is greater than Maximum Mark.')                            
                        mark.mark = markgrade

                    if (is_update):
                        marks_update.append(mark)
                    else:
                        marks.append(mark)

        if not exam.is_grade:
            if not SubjectMarkConf.objects.filter(exam=exam, subject_id=subject):
                SubjectMarkConf.objects.create(
                    exam=exam, subject_id=subject, max_mark = request.POST['max_mark'], pass_mark = request.POST['pass_mark']) 

        # Bulk Update
        if exam.is_grade:
            Marks.objects.bulk_update(marks_update, ['grade'])
        else:
            Marks.objects.bulk_update(marks_update, ['mark'])
        Marks.objects.bulk_create(marks)
        return HttpResponse('success')


class ExamReports(TeacherRequiredMixin, View):
    def get(self, request):
        resp ={'academicyears': AcademicYear.objects.all()}        
        rep_year = request.GET.get('academicyear','')
        resp['rep_classroom'] = request.GET.get('classroom','')
        resp['rep_exam'] = request.GET.get('exam','')
        if rep_year:
            resp['rep_year'] = int(rep_year)

        if resp['rep_classroom'] and resp['rep_exam']:
            resp['students'] = []
            for student in Student.objects.filter(classroom=resp['rep_classroom']):
                totalmarks = Marks.objects.filter(exam = resp['rep_exam'],
                        student=student).aggregate(Sum('mark'))['mark__sum']
                if totalmarks != None:
                    resp['students'].append({
                        'id': student.user.id,
                        'name': student.user.get_full_name(),
                        'totalmarks': totalmarks
                    })
        return render(request,'exams/examreports.html', resp)

class BarChart(TeacherRequiredMixin, View):
    def get(self, request, **kwargs):
        # Marks(exam, subject,student, mark)
        exam = Exam.objects.get(id = kwargs['exam'])
        student = Student.objects.get(user_id = kwargs['student'])
        subjectmarks = [
            [mark.subject.name, mark.mark]
            for mark in Marks.objects.filter(exam=exam,student=student)
        ]
        # subjectmarks = [['Shanghai', 24.2],['Beijing', 20.8]]
        resp = {'subjectmarks':subjectmarks,'exam':exam, 'student': student}
        
        return render(request,'exams/barchart.html', resp)



class getAjaxJson(TeacherRequiredMixin, View):
    """
    Used in Markentry
    * When Exam or Subject select box change fill Division select box
    * When Division select box change load students in Handsontable
    Used in ExamReport
    * To fill Classroom select box
    """
    def getHandsontableData(self, school,exam, classroomid, subject):
        # fill handsontable 
        classroom = ClassRoom.objects.get(school = school, id = classroomid)
        marks = Marks.objects.filter(exam=exam,subject=subject)
        students=[]
        for s in Student.objects.filter(classroom=classroom, user__is_staff=True):
            data = [s.user.id, s.user.get_full_name(), '']
            has_mark = marks.filter(student=s)
            if has_mark:
                data[2] = has_mark[0].markgrade
            students.append(data)
        return students

    
    def get(self, request):
        school = request.user.school
        exam = Exam.objects.get(school=school, id=request.GET['exam'])
        classroom = request.GET.get('classroom',None)
        resp = {'is_grade':exam.is_grade}
        if classroom:
            resp['students'] = self.getHandsontableData(school, exam,classroom, request.GET['subject'])
        else:
            # fill ClassRoom select box
            subject = request.GET.get('subject',None)
            if not exam.is_grade and subject:
                # to fill maxmark and passmark input boxes
                sub_conf = SubjectMarkConf.objects.filter(exam=exam,subject=subject)
                if sub_conf:
                    resp['sub_conf'] = [sub_conf[0].max_mark, sub_conf[0].pass_mark]
                else:
                    resp['sub_conf'] = ['','']
            resp['classes']= [{'classroom':c.classname,'id' :c.id} 
                for c in ClassRoom.objects.filter(school = school, name=exam.exam_class)]
        return JsonResponse(resp,safe=False)

class getExams(TeacherRequiredMixin, View):
    """
    Used in ExamReport
    * To fill Exams select box
    """
    def get(self, request):
        exams = [{'id':e.id,'name':e.name} for e in 
            Exam.objects.filter(school=request.user.school, 
                academicyear=request.GET['ayear']).order_by('exam_date')]
        return JsonResponse({'exams':exams},safe=False)
