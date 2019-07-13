from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.urls import reverse

from teachers.decorators import teacher_required
from .models import ClassRoom, Subject, Period
from .forms import ClassroomForm,PeriodForm, SubjectForm

# Create your views here.
@method_decorator([login_required, teacher_required], name='dispatch')
class TimeTableView(View):
    def get(self, request):
        school = request.user.school
        classroom_name = request.GET.get('classroom','')
        if classroom_name: 
            classroom = ClassRoom.objects.get(school = school, name = classroom_name)
            periods = Period.objects.filter(classroom= classroom)            

            qs_json = [{
                'id':p.id, 
                'title':'{0}\n{1}'.format(p.subject.name, p.teacher.username), 
                'start':p.startdatetime,
                'end':p.enddatetime
                } for p in periods]
            return JsonResponse(qs_json,safe=False)

        
        resp = {
            'classrooms': ClassRoom.objects.filter(school = school),
            'subjects': Subject.objects.filter(school = school),
            'teachers': get_user_model().objects.filter(school = school, user_type=2),
        }
        
        return render(request,'classroom/timetable.html', resp)

    def post(self,request):
        """
        Save a Period of TimeTable
        """
        # classroom, subject, teacher, day, starttime,endtime
        school = request.user.school
        DAY_CHOICES = {n[1]: n[0] for n in Period._meta.get_field('dayoftheweek').choices}
        updated_request = request.POST.copy()
        updated_request['classroom'] = ClassRoom.objects.get(school = school,name=updated_request['classroom']).id
        updated_request['dayoftheweek'] = DAY_CHOICES[updated_request['dayoftheweek']]
        form = PeriodForm(updated_request)
        if form.is_valid():
            form.save()
            message = 'success'
        else:
            message = str(form.errors)

        return HttpResponse(message)


def classroom_view(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.school = request.user.school
            classroom.save()
            messages.success(request, 'ClassRoom saved with success!')
            return redirect('classroom:classrooms')
    else:
        classroom = ClassRoom(school = request.user.school)
        form = ClassroomForm(instance=classroom)

    classrooms = ClassRoom.objects.filter(school = request.user.school)
    return render(request,"classroom/classrooms.html", {'form': form, 'classrooms':classrooms })

def subject_view(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.school = request.user.school
            subject.save()
            messages.success(request, 'Subject saved with success!')
            return redirect('classroom:subjects')
    else:
        subject = Subject(school = request.user.school)
        form = SubjectForm(instance=subject)

    subjects = Subject.objects.filter(school = request.user.school)
    return render(request,"classroom/subjects.html", {'form': form, 'subjects':subjects })
