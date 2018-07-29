from django.urls import include, path
from django.contrib import admin
from schools.views import SignUpView,Profile, home,load_courses
from students.views import StudentSignUpView
from teachers.views import TeacherSignUpView
urlpatterns = [
	path('', home, name='home'),
	path('admin/', admin.site.urls),
    path('schools/', include(('schools.urls','schools'),namespace='schools')),
    path('students/', include(('students.urls','students'),namespace='students')),
    path('teachers/', include(('teachers.urls','teachers'),namespace='teachers')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', Profile.as_view(), name='profile'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/student/ajax/load-courses/', load_courses, name='ajax_load_courses'),
    path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]