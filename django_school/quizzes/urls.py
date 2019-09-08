from django.urls import include, path

from quizzes.views import student, teacher

urlpatterns = [
    path('s/', student.QuizListView.as_view(), name='quiz_list'),
    path('s/interests/', student.StudentInterestsView.as_view(), name='student_interests'),
    path('s/taken/', student.TakenQuizListView.as_view(), name='taken_quiz_list'),
    path('s/<int:pk>/', student.take_quiz, name='take_quiz'),
    path('s/<int:pk>/studentresults/', student.QuizResultsView.as_view(), name='student_quiz_results'),

    # Teacher urls
	path('t/', teacher.QuizListView.as_view(), name='quiz_change_list'),
    path('t/add/', teacher.QuizCreateView.as_view(), name='quiz_add'),
    path('t/change/<int:pk>/', teacher.QuizUpdateView.as_view(), name='quiz_change'),
    path('t/<int:pk>/delete/', teacher.QuizDeleteView.as_view(), name='quiz_delete'),
    path('t/<int:pk>/results/', teacher.QuizResultsView.as_view(), name='quiz_results'),
    
    path('t/<int:pk>/question/add/', teacher.question_add, name='question_add'),
    path('t/<int:quiz_pk>/question/<int:question_pk>/', 
    	teacher.question_change, name='question_change'),
    path('t/<int:quiz_pk>/question/<int:question_pk>/delete/', 
    	teacher.QuestionDeleteView.as_view(), name='question_delete'),
]