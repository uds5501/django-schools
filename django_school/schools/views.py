from django.shortcuts import redirect, render
from django.views import View, generic
from django.contrib import messages
from .models import Course, School

class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'

def load_courses(request):
    import time
    time.sleep(3)
    school_id = request.GET.get('school')
    courses = Course.objects.filter(school_id=school_id).order_by('name')
    return render(request, 'registration/course_dropdown_list_options.html', {'courses': courses})

def home(request):    
    if not request.user.is_authenticated: 
        return redirect('schools:districts')
    
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

def districts(request):
    districts = [
        'thiruvananthapuram','kollam','pathanamthitta',
        'alappuzha','kottayam','idukki', 'ernakulam',
        'thrissur', 'palakkad', 'malappuram', 'kozhikode',
        'wayanad', 'kannur', 'kasaragod',
    ]
    c_districts = [[d,School.objects.filter(district__iexact=d).count()] for d in districts]
    
    return render(request,'schools/districts.html',{'districts':c_districts})

def sub_districts(request,district):
    from .sub_districts import SUB_DISTRICTS
    return render(request,'schools/sub_districts.html',{'sub_districts':SUB_DISTRICTS[district-1]})

def school_view(request,code):
    school = School.objects.get(code = code)
    return render(request,'schools/school.html',{'school':school})

from django.http import JsonResponse
import json
def search(request):
    q_ajax = request.GET.get('q','')
    if q_ajax: 
        s = School.objects.filter(name__icontains = q_ajax)[:20].values('id','name')
        return JsonResponse({"results": list(s)},safe=False)
    
    sub_district = request.GET.get('sub_district','')
    name = request.GET.get('name','')
    query = None
    if name: 
        # filtered by name
        schools = School.objects.filter(name__icontains = name)[:20]
        query = name
    elif sub_district: 
        # filtered by dist
        schools = School.objects.filter(sub_district__iexact = sub_district)
        query = sub_district
    else:
        schools = School.objects.order_by('-created_on')[:10]

    return render(request,'schools/search.html',{'schools':schools,'q':query})


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