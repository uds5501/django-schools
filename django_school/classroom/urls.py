from django.urls import include, path
from django.views.generic import TemplateView
from classroom.views import TimeTableView

urlpatterns = [
	path('', TemplateView.as_view(template_name="classroom/classrooms.html"), name='classrooms'),
	path('timetable/', TimeTableView.as_view(), name='timetable'),
	# path('timetable', TemplateView.as_view(template_name="classroom/timetable.html"), name='timetable'),
]