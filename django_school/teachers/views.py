from django.views import View

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.conf import settings
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse,JsonResponse
import json

from students.models import Student
from schools.models import Event

from .decorators import teacher_required
from .forms import TeacherSignUpForm

class TeacherSignUpView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['usertype'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



@method_decorator([login_required, teacher_required], name='dispatch')
class EventList(View):
    def get(self, request):
        flag = request.GET.get('json','')
        if flag: 
            events= Event.objects.filter(school = request.user.school)
            qs_json = [dict(id=et.id, title=et.title, start=str(et.startdatetime)) for et in events]
            return JsonResponse(qs_json,safe=False)

        return render(request,'teachers/events.html')

    def post(self,request):
        from datetime import datetime
        title = request.POST.get('title','')
        event_time = request.POST.get('time','')
        if len(request.POST['title'])<3: 
            msg='Title must have atleast 3 characters'
        elif not event_time:
            msg = 'You must select event time'
        else:                
            event_datetime = '%s %s' %(request.POST.get('date'),request.POST.get('time'))
            event = Event.objects.create(school=request.user.school,
                title = request.POST.get('title') ,
                startdatetime = datetime.strptime(event_datetime,"%Y-%m-%d %I:%M%p"))
            msg = 'success'

        return HttpResponse(msg)
