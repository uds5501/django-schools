from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.exam_view, name='exams'),
    path('markentry/', views.MarkEntry.as_view(), name='markentry'),
    path('getdivisions/', views.getDivisions.as_view(), name='getdivisions'),
    
]