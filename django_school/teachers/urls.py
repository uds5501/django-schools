from django.urls import include, path

from . import views as teachers

urlpatterns = [
    path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/', 
    	teachers.question_change, name='question_change'),
]