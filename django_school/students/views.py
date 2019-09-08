from django.conf import settings
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

from schools.models import Event
from classroom.views.timetable import get_timetable_periods

from .decorators import student_required
from .forms import StudentSignUpForm

class StudentSignUpView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['usertype'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')#students:quiz_list')


@method_decorator([login_required, student_required], name='dispatch')
class EventList(View):
    def get(self, request):
        flag = request.GET.get('json','')
        if flag: 
            events= Event.objects.filter(school = request.user.school)
            qs_json = [dict(id=et.id, title=et.title, start=str(et.startdatetime)) for et in events]
            return JsonResponse(qs_json,safe=False)

        return render(request,'students/events.html')


@method_decorator([login_required,student_required], name='dispatch')
class TimeTableView(View):
    def get(self, request):
        qs_json = get_timetable_periods(request.user.student.classroom)
        return JsonResponse(qs_json,safe=False)
        