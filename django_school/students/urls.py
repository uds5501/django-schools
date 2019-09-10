from django.urls import include, path, re_path

from . import views as students
# from django.views.generic import TemplateView

urlpatterns = [
	path('student_import/', students.StudentImport.as_view(), name='student_import'),
	# re_path(r'^users/(?P<usertype>[0-9])/$', students.UserList.as_view(), name='user_list'),
	re_path(r'^(?P<usertype>[2-9])/$', students.UserList.as_view(), name='user_list'),
	path('', students.UserList.as_view(), name='user_list'),
	# other urls
	path('events/', students.EventList.as_view(), name='events'),

	# path('attendance/', students.AttendanceView.as_view(), name='attendance'),
    # path('timetable/', students.TimeTableView.as_view(), name='timetable'),
]