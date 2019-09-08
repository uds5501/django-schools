from django.conf import settings
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth import get_user_model

from schools.models import Event
from classroom.views.timetable import get_timetable_periods
from teachers.decorators import teacher_required

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

@method_decorator([login_required, teacher_required], name='dispatch')
class UserList(View):
    def get(self, request, usertype="1"):
        # if not usertype: usertype = 1
        queryset = get_user_model().objects.filter(school = request.user.school, user_type = usertype)
        return render(request,'students/user_list.html',{'users':queryset,'page': usertype})

    def post(self,request, usertype="1"):
        user_id = request.POST.get('user','')
        verified = request.POST.get('verified', '')
        if user_id:
            user = get_user_model().objects.get(id = user_id)
            if verified == 'on': 
                user.is_staff = True
            else:
                user.is_staff = False
            user.save()

        if usertype=="1":
            return redirect('students:user_list')
        return redirect('students:user_list', usertype)

@method_decorator([login_required, teacher_required], name='dispatch')
class StudentImport(View):
    def get(self, request):
        return render(request,'students/student_import.html')

    def post(self,request):
        import json
        for row in json.loads(request.POST['data']):
            print(row)
        return HttpResponse('success')