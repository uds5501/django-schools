import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model

from schools.mixins import TeacherRequiredMixin
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

    # def set_mark_grade(self):
    #     pass

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

class getAjaxJson(TeacherRequiredMixin, View):
    """
    Used for
    * When Exam or Subject select box change fill Division select box
    * When Division select box change load students in Handsontable
    """
    def get(self, request):
        school = request.user.school
        exam = Exam.objects.get(school=school, id=request.GET['exam'])
        division = request.GET.get('division',None)
        resp = {'is_grade':exam.is_grade}
        if division:
            # fill handsontable 
            classroom = ClassRoom.objects.get(school = school, name=exam.exam_class, division = division)
            marks = Marks.objects.filter(exam=exam,subject=request.GET['subject'])
            resp['students']=[]
            for s in Student.objects.filter(classroom=classroom, user__is_staff=True):
                data = [s.user.id, s.user.get_full_name(), '']
                has_mark = marks.filter(student=s)
                if has_mark:
                    data[2] = has_mark[0].markgrade
                resp['students'].append(data)
        else:
            # fill division select box
            if not exam.is_grade:
                # to fill maxmark and passmark input boxes
                sub_conf = SubjectMarkConf.objects.filter(exam=exam,subject=request.GET['subject'])
                if sub_conf:
                    resp['sub_conf'] = [sub_conf[0].max_mark, sub_conf[0].pass_mark]
                else:
                    resp['sub_conf'] = ['','']
            resp['classes']= [{'classroom':c.classname,'division' :c.division} for c in ClassRoom.objects.filter(school = school, name=exam.exam_class)]
        return JsonResponse(resp,safe=False)