from django.urls import include, path, re_path

from . import views as students
# from django.views.generic import TemplateView

urlpatterns = [
	path('student_import/', students.StudentImport.as_view(), name='student_import'),
	path('student_migration/', students.StudentMigrationView.as_view(), name='student_migration'),
	path('getajaxstudents/', students.getAjaxStudents.as_view(), name='getajaxstudents'),
	re_path(r'^(?P<usertype>[2-9])/$', students.UserList.as_view(), name='user_list'),
	path('', students.UserList.as_view(), name='user_list'),
	# other urls
	path('events/', students.EventList.as_view(), name='events'),

	# path('attendance/', students.AttendanceView.as_view(), name='attendance'),
    # path('timetable/', students.TimeTableView.as_view(), name='timetable'),
]