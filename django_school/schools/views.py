from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            # please class teacher or principal to activate
            return render(request,'registration/inactive_user.html')
        if request.user.is_superuser:
            return render(request,'home.html')
        elif request.user.is_teacher:
            #return redirect('quiz_change_list')
            return render(request,'teachers/home.html')
        elif request.user.is_student:        	
            #return redirect('quiz_list')
            return render(request,'students/home.html')
        
    return render(request, 'home.html')