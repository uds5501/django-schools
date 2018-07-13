from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'home.html')
        elif request.user.is_teacher:
            return redirect('quiz_change_list')
        else:
            return redirect('quiz_list')
    return render(request, 'home.html')