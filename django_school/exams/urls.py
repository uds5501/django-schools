from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.exam_view, name='exam'),
    # path('classrooms/', classroom.classroom_view, name='classrooms'),
]