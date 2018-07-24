from django.urls import include, path

from . import views as students
from django.views.generic import TemplateView

urlpatterns = [
	path('attendance/', TemplateView.as_view(template_name="students/attendance.html"), name='attendance'),
    path('quizzes/', students.QuizListView.as_view(), name='quiz_list'),
    path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
    path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
    path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
]