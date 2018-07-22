from django.urls import include, path

from . import views as teacher_views
from quizzes import views as quizzes_views
from django.views.generic import TemplateView

urlpatterns = [
    # students
    path('students/', teacher_views.StudentList.as_view(), name='student_list'),
    path('events/', teacher_views.EventList.as_view(), name='events'),

    # quiz urls
	path('quizzes/', quizzes_views.QuizListView.as_view(), name='quiz_change_list'),
    path('quiz/add/', quizzes_views.QuizCreateView.as_view(), name='quiz_add'),
    path('quiz/<int:pk>/', quizzes_views.QuizUpdateView.as_view(), name='quiz_change'),
    path('quiz/<int:pk>/delete/', quizzes_views.QuizDeleteView.as_view(), name='quiz_delete'),
    path('quiz/<int:pk>/results/', quizzes_views.QuizResultsView.as_view(), name='quiz_results'),
    
    path('quiz/<int:pk>/question/add/', teacher_views.question_add, name='question_add'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/', 
    	teacher_views.question_change, name='question_change'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', 
    	quizzes_views.QuestionDeleteView.as_view(), name='question_delete'),
]
