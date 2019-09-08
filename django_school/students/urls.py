from django.urls import include, path

from . import views as students
from django.views.generic import TemplateView

urlpatterns = [
	path('events/', students.EventList.as_view(), name='events'),
	path('attendance/', TemplateView.as_view(template_name="students/attendance.html"), name='attendance'),
    # path('quizzes/', students.QuizListView.as_view(), name='quiz_list'),
    # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
    # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
    # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    # path('quiz/<int:pk>/studentresults/', students.QuizResultsView.as_view(), name='student_quiz_results'),
    path('timetable/', students.TimeTableView.as_view(), name='timetable'),
]