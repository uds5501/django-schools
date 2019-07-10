from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse

from teachers.decorators import teacher_required
from .models import ClassRoom, Subject, Period


# Create your views here.
@method_decorator([login_required, teacher_required], name='dispatch')
class TimeTableView(View):
    def get(self, request):
        school = request.user.school
        classroom_name = request.GET.get('classroom','')
        if classroom_name: 
            print(request.GET['start'],request.GET['end'])
            classroom = ClassRoom.objects.get(school = school, name = classroom_name)
            periods = Period.objects.filter(classroom= classroom)
            
            qs_json = [{'id':p.id, 'title':p.subject.name, 'start':'2019-01-01T13:30:00','end':'2019-01-01T14:30:00'} for p in periods]
            # print(qs_json)
            return JsonResponse(qs_json,safe=False)

        
        resp = {
            'classrooms': ClassRoom.objects.filter(school = school),
            'subjects': Subject.objects.filter(school = school),
            'teachers': get_user_model().objects.filter(school = school, user_type=2),
        }

        

            # events= Event.objects.filter(school = request.user.school)
            # qs_json = [dict(id=et.id, title=et.title, start=str(et.startdatetime)) for et in events]
            # return JsonResponse(qs_json,safe=False)

        
        return render(request,'classroom/timetable.html', resp)

    def post(self,request):
        """
        Save a Period of TimeTable
        """
        print(request.POST)
        return HttpResponse('success')
