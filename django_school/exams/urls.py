from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.exam_view, name='exams'),
    path('markentry/', views.MarkEntry.as_view(), name='markentry'),
    path('getajaxdata/', views.getAjaxJson.as_view(), name='getajaxdata'),
    
]