from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.exam_view, name='exams'),
    path('markentry/', views.MarkEntry.as_view(), name='markentry'),    
    path('examreports/', views.ExamReports.as_view(), name='examreports'),
    path('barchart/<int:exam>/<int:student>/', views.BarChart.as_view(), name='barchart'),

    # AJAX JSON FETCH URLS
    path('getajaxdata/', views.getAjaxJson.as_view(), name='getajaxdata'),
    path('getajaxexams/', views.getExams.as_view(), name='getajaxexams'),    
]