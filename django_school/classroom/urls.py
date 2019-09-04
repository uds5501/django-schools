from django.urls import include, path
from django.views.generic import TemplateView
from classroom.views import (TimeTableView,AttendanceView, classroom_view, 
	AttendanceReportView,	subject_view, delete_period)

urlpatterns = [
	path('', AttendanceView.as_view(), name='attendance'),
	path('attendancereport/', AttendanceReportView.as_view(), name='attendancereport'),
	path('classrooms/', classroom_view, name='classrooms'),
	path('subjects/', subject_view, name='subjects'),
	path('deleteperiod/', delete_period, name="deleteperiod"),
	path('timetable/', TimeTableView.as_view(), name='timetable'),
	
	# path('timetable', TemplateView.as_view(template_name="classroom/timetable.html"), name='timetable'),
]

