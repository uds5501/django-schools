from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import Course
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def load_courses(request):
    school_id = request.GET.get('school')
    courses = Course.objects.filter(school_id=school_id).order_by('name')
    return render(request, 'registration/course_dropdown_list_options.html', {'courses': courses})

def home(request):    
    if not request.user.is_authenticated: return redirect('login')

    """
    if not request.user.is_staff:
        # please class teacher or principal to activate
        return render(request,'registration/inactive_user.html')
    """       
    if request.user.is_teacher:
        #return redirect('quiz_change_list')
        return render(request,'teachers/home.html')
    elif request.user.is_student:        	
        #return redirect('quiz_list')
        return render(request,'students/home.html')    

    # some other users, eg: principal
    return render(request, 'home.html')