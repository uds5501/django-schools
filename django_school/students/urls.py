from django.urls import include, path

from . import views as students

urlpatterns = [
    path('', students.QuizListView.as_view(), name='quiz_list'),
    path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
    path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
    path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
]