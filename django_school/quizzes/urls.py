from django.urls import include, path

from . import views as quizzes_views

urlpatterns = [
	path('', quizzes_views.QuizListView.as_view(), name='quiz_change_list'),
    path('quiz/add/', quizzes_views.QuizCreateView.as_view(), name='quiz_add'),
    path('quiz/<int:pk>/', quizzes_views.QuizUpdateView.as_view(), name='quiz_change'),
    path('quiz/<int:pk>/delete/', quizzes_views.QuizDeleteView.as_view(), name='quiz_delete'),
    path('quiz/<int:pk>/results/', quizzes_views.QuizResultsView.as_view(), name='quiz_results'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', 
    	quizzes_views.QuestionDeleteView.as_view(), name='question_delete'),
]