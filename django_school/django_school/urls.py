from django.urls import include, path
from django.contrib import admin
from schools.views import SignUpView,home
from students.views import StudentSignUpView
from teachers.views import TeacherSignUpView
urlpatterns = [
	path('', home, name='home'),
	path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]