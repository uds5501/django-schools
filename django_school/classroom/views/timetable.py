from django.views import View
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from schools.mixins import TeacherRequiredMixin
from classroom.models import ClassRoom, Subject, Period
from classroom.forms import PeriodForm

def get_timetable_periods(classroom):
    color_list = ['#008744','#0057e7','#d62d20','#ffa700','#ffffff',
            '#96ceb4','#ffeead','#ff6f69','#ffcc5c','#88d8b0',
            '#ffb3ba','#ffdfba','#ffffba','#baffc9','#bae1ff',]
    
    periods = Period.objects.filter(classroom= classroom)
    return [{
        'id':p.id, 
        'title':'{0} ({1})'.format(p.subject.name, p.teacher.username), 
        'start':p.startdatetime,
        'end':p.enddatetime,
        'color': color_list[p.subject.id % len(color_list)]
        } for p in periods]


class TimeTableView(TeacherRequiredMixin,View):
    def get(self, request):
        school = request.user.school
        classroom_name = request.GET.get('classroom','')
        
        if classroom_name: 
            classroom = ClassRoom.objects.get(school = school, name = classroom_name)
            qs_json = get_timetable_periods(classroom)
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


class DeletePeriodView(TeacherRequiredMixin,View):
    def get(self, request):
        p = Period.objects.get(id=request.GET['period']).delete()
        return HttpResponse('success')


