from datetime import date, datetime,timedelta
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from schools.mixins import StudentRequiredMixin
from classroom.views.timetable import get_timetable_periods
from classroom.models import Attendance

class HomeView(StudentRequiredMixin, View):

    def get(self, request):
        resp = {'year': date.today().year, 'month': date.today().month -1}
        return render(request,'dashboard/home.html',resp)


class TimeTableView(StudentRequiredMixin, View):
    def get(self, request):
        qs_json = get_timetable_periods(request.user.student.classroom)
        return JsonResponse(qs_json,safe=False)
        
class AttendanceView(StudentRequiredMixin, View):

    def get(self, request):
        middle  = timedelta(days=15)
        start = datetime.fromtimestamp(int(request.GET['start'])) + middle
        attendances = Attendance.objects.filter(
            student__user=request.user, 
            attendanceclass__date__year = start.year,
            attendanceclass__date__month = start.month,
        )
        # print(attendances)
        resp = {}
        for attendance in attendances:
            item = int(attendance.attendanceclass.date.strftime("%s%f"))/1000000
            status = 2 if attendance.status == 'P' else 3
            resp[str(item)]=status
        # present = int(date(2019,1,15).strftime("%s%f"))/1000000
        
        return JsonResponse(resp,safe=False)