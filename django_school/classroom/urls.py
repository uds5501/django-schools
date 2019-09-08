from django.urls import include, path
from django.views.generic import TemplateView

from classroom.views import timetable, attendance, classroom, subject

urlpatterns = [
	path('', attendance.AttendanceView.as_view(), name='attendance'),
	path('attendancereport/', attendance.AttendanceReportView.as_view(), name='attendancereport'),
	path('classrooms/', classroom.classroom_view, name='classrooms'),
	path('subjects/', subject.subject_view, name='subjects'),
	path('deleteperiod/', timetable.DeletePeriodView.as_view(), name="deleteperiod"),
	path('timetable/', timetable.TimeTableView.as_view(), name='timetable'),
	
	# path('timetable', TemplateView.as_view(template_name="classroom/timetable.html"), name='timetable'),
]

