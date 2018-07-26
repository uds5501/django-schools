from django.shortcuts import redirect, render
from django.views import View, generic
from django.contrib import messages
from .models import Course
class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'

def load_courses(request):
    school_id = request.GET.get('school')
    courses = Course.objects.filter(school_id=school_id).order_by('name')
    return render(request, 'registration/course_dropdown_list_options.html', {'courses': courses})

def home(request):    
    if not request.user.is_authenticated: return redirect('login')
    
    if not request.user.is_staff:
        # please class teacher or principal to activate
        return render(request,'registration/inactive_user.html')
         
    if request.user.is_teacher:
        #return redirect('quiz_change_list')
        return render(request,'teachers/home.html')
    elif request.user.is_student:        	
        #return redirect('quiz_list')
        return render(request,'students/home.html')    

    # some other users, eg: principal,admin
    return render(request, 'home.html')

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator([login_required], name='dispatch')
class Profile(View):
    # even inactive users can view/edit their profile
    def get(self, request):
        return render(request,'profile.html')

    def post(self,request):
        user_id=request.POST['user']

        user = request.user #User.objects.get(id = user_id)
        user.first_name = request.POST.get('first_name','')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'User details of %s saved with success!' % user.username)
        return redirect('profile')