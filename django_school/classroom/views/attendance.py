from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse

from students.models import Student
from schools.models import AcademicYear
from schools.mixins import TeacherRequiredMixin

from classroom.models import ClassRoom,Attendance, AttendanceClass


class AttendanceView(TeacherRequiredMixin, View):
    def get(self, request):
        school = request.user.school
        classrooms = ClassRoom.objects.filter(school=school).order_by('name')
        resp = {'classrooms': classrooms, 'students': None, 'attendances': None}

        att_classroom = request.GET.get('classroom','')
        att_date = request.GET.get('date','')

        if att_classroom:
            resp['att_classroom'] = int(att_classroom)
        resp['att_date'] = att_date
        if att_classroom and att_date:
            # dt = datetime.strptime(att_date, "%d/%m/%Y")
            attendance_config = AttendanceClass.objects.filter(
                academicyear__status = True,
                classroom_id = att_classroom,
                date = datetime.strptime(att_date, '%d/%m/%Y')
            )
            resp['students'] = Student.active_objects.filter(classroom_id = att_classroom)
            if attendance_config:

                resp['attendances'] = attendance_config[0].attendance_set.all()

            # resp['attendance_status_choices'] = Attendance.ATTENDANCE_STATUS_CHOICES
            # Period.objects.filter(classroom_id = request.GET['classroom'],
            #    dayoftheweek = dt.weekday()).order_by('starttime')
            # print(resp['students'].values())
        # print(resp)
        return render(request,'classroom/attendance.html', resp)

    def post(self,request):
        """
        Add / Edit attendance entries
        """ 
        att_classroom = request.POST['classroom']
        att_date = request.POST['date']
        # datetime.strptime("2013-1-25", '%d/%m/%Y').strftime('%Y-%m-%d')
        attendance_config, _ = AttendanceClass.objects.get_or_create(
            academicyear = AcademicYear.objects.get(status=True),
            classroom_id = att_classroom,
            date = datetime.strptime(att_date, '%d/%m/%Y')
            )
        for student in Student.active_objects.filter(classroom_id = att_classroom):
            status = request.POST[str(student.user.id)]
            if status == 'present':
                status = 'P'
            else:
                status = 'A'

            Attendance.objects.update_or_create(
                attendanceclass=attendance_config,
                student=student,
                defaults={'status':status})
        messages.success(request, 'Attendance details saved with success!')
        urlparams = "?classroom={}&date={}".format(att_classroom,att_date)
        return redirect(reverse('classroom:attendance')+urlparams)

class AttendanceReportView(TeacherRequiredMixin, View):
    def generate_report(self,att_class):
        """
        {'suhail': {2: 'A', 3: 'P', 4: 'P'}, 'sufail': {2: 'P', 4: 'P'}, 'sulaiman': {2: 'P', 4: 'P'}}
        """        
        transposed = {}
        for att in att_class:
            for attendance in att.attendance_set.all():
                transposed.setdefault(attendance.student.user.username, {}).update(
                                {att.date.day: attendance.status})
        return transposed

    def get(self, request):
        school = request.user.school
        classrooms = ClassRoom.objects.filter(school=school).order_by('name')
        resp = {'classrooms': classrooms, 'academicyears': AcademicYear.objects.all(), 'attendances': None,
            'months': ['January','February','March','April','May','June','July','August','September','October','November','December']}

        att_classroom = request.GET.get('classroom','')
        att_year = request.GET.get('academicyear','')
        att_month = request.GET.get('month','')
        if att_classroom:
            resp['att_classroom'] = int(att_classroom)
        if att_year:
            resp['att_year'] = int(att_year)
        if att_month:
            resp['att_month'] = int(att_month)

        if att_classroom and att_year and att_month:
            # dt = datetime.strptime(att_date, "%d/%m/%Y")
            att_class = AttendanceClass.objects.filter(
                academicyear_id = att_year,
                classroom_id = att_classroom,
                date__month = att_month
            ).order_by('date')
            resp['attendances'] = self.generate_report(att_class)
            resp['days'] = range(1,32)
        return render(request,'classroom/attendancereport.html', resp)
