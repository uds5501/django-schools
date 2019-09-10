from django.urls import path

from . import views 
# from django.views.generic import TemplateView

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('attendance/', views.AttendanceView.as_view(), name='attendance'),
    path('timetable/', views.TimeTableView.as_view(), name='timetable'),
]