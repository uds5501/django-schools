import json, re

from django.conf import settings
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.db.models import Max

from schools.mixins import StudentRequiredMixin, TeacherRequiredMixin
from schools.models import Event, AcademicYear
from classroom.models import ClassRoom
from classroom.views.timetable import get_timetable_periods
from teachers.decorators import teacher_required

from .decorators import student_required
from .forms import StudentSignUpForm
from .models import Student, StudentMigration

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
        classrooms = ClassRoom.objects.filter(school = request.user.school)
        return render(request,'students/student_import.html',{'classrooms':classrooms })

    def post(self,request):
        classroom = request.POST['classroom']
        if not classroom:
            return HttpResponse('Please select a ClassRoom.')
        User = get_user_model()
        users = []
        for row in json.loads(request.POST['data']):
            if any(row):
                if all(row):
                    fname,lname,email,dob = row
                    if User.objects.filter(username=email):
                        return HttpResponse('Email:{} already exists. Please provide different email.'.format(email))
                    user = User(
                        first_name=fname, last_name=lname, is_staff=True,
                        username=email, email=email, user_type=1, school=request.user.school
                    )
                    user.set_password(dob)
                    users.append(user)
                    # user = get_user_model().objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
                else:
                    return HttpResponse('All fields are required.')

        academicyear = AcademicYear.objects.get(status=True)
        for user in users:
            user.save()
            student = Student.objects.create(user=user,classroom_id = classroom)
            StudentMigration.objects.create(student = student, classroom_id = classroom, academicyear = academicyear)

        # User.objects.bulk_create(users)
        return HttpResponse('success')


class StudentMigrationView(TeacherRequiredMixin, View):
    def get(self, request):
        """
        View to list of students of a particular class for migration
        """
        classrooms = ClassRoom.objects.filter(school = request.user.school)
        return render(request,'students/student_migration.html', {'classrooms':classrooms})

    def post(self, request):
        academicyear = AcademicYear.objects.get(status=True)
        school = request.user.school
        migrations = []
        students = []
        for row in json.loads(request.POST['data']):
            # [3, 'Suhail  VS', 'Passed Out', '']
            pass_status = row[2]
            student = get_user_model().objects.get(id =row[0]).student
            
            if(pass_status == 'Passed Out'):
                migrations.append(StudentMigration(student = student, academicyear = academicyear, status = 'Passout'))
                student.classroom = None
                
            else:
                name,division = re.split(r'(\d+)', row[3])[1:3]
                try:
                    classroom = ClassRoom.objects.get(school = school, name = name, division=division)
                except ClassRoom.DoesNotExist:
                    return HttpResponse('Classroom {} does not exist.'.format(row[3]))
                
                migrations.append(StudentMigration(
                    student = student, 
                    academicyear = academicyear,
                    classroom = classroom,
                    status = pass_status
                ))
                student.classroom = classroom
            students.append(student)
            # break

        StudentMigration.objects.bulk_create(migrations)
        Student.objects.bulk_update(students,['classroom'])
        return HttpResponse('success')

class getAjaxStudents(TeacherRequiredMixin, View):
    """
    Used in Student Migration
    * When Classroom select box change load students in Handsontable
    """
    def get(self, request):
        # fill handsontable 
        classroom = request.GET.get('classroom','')
        students = []
        if classroom:
            classroom = ClassRoom.objects.get(id=classroom)
            academicyear = AcademicYear.objects.get(status = True)
            student_migrations = StudentMigration.objects.filter(
                classroom = classroom, 
                academicyear = academicyear
            )

            queryset = Student.objects.filter(classroom = classroom)
            maxclass = ClassRoom.objects.filter(school=request.user.school).aggregate(Max('name'))

            ht_status, ht_class = 'Passed', '{}{}'.format(classroom.name + 1, classroom.division)
            if maxclass['name__max'] == classroom.name:
                ht_status='Passed Out'
                ht_class = ''

            for s in queryset:            
                if student_migrations.filter(student=s):
                    # Skip if student already migrated
                    print('skipping:', s.user.first_name)
                    continue

                students.append([s.user.id, s.user.get_full_name(), ht_status, ht_class])

        return JsonResponse({'students':students},safe=False)