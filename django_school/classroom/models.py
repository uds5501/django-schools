from datetime import datetime, date, timedelta
from django.db import models
from django.conf import settings

from schools.models import School, AcademicYear
from students.models import Student
# Create your models here.

class ClassRoom(models.Model):
    # Class for exampl: 8A, 7B, 10I etc
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    name = models.SmallIntegerField()
    division = models.CharField(max_length=2)
    #teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    # i don't know whether the below things are required or not
    # teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    # students = models.ManyToManyField(User, related_name="course_students",blank=True)

    class Meta:
        unique_together = ("school", "name", "division")
    
    def __str__(self):
        return f'{self.name}-{self.division}'

    #def get_absolute_url(self):
    #    return reverse('course_detail', args=[str(self.id)])

class Subject(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Period(models.Model):
    # A Period will just be a recurring Event(every week) related to a Classroom.
    
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    starttime = models.TimeField()
    endtime = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    dayoftheweek = models.IntegerField(choices=DAY_CHOICES)

    def getdatetime(self, time):
        d = date(2018, 12, 31)
        dayoftheweek = self.DAY_CHOICES[self.dayoftheweek][0]
        d += timedelta(dayoftheweek)
        dt = datetime.combine(d, time)
        return dt.strftime('%Y-%m-%dT%H:%M:%S')


    @property
    def startdatetime(self):
        return self.getdatetime(self.starttime)
    
    @property
    def enddatetime(self):
        return self.getdatetime(self.endtime)

    def __str__(self):
        # return f"{self.classroom.name} - {self.subject} on {self.DAY_CHOICES[self.dayoftheweek][1]} {self.starttime}"
        return "{0} - {1} on {2} {3}".format(self.classroom.name, self.subject, self.DAY_CHOICES[self.dayoftheweek][1], self.starttime)


class AttendanceClass(models.Model):
    academicyear = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    date = models.DateField()


class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('H', 'Half Day'),
        ('L', 'Leave'),
        ('N', 'Not Marked'),
    ]

    attendanceclass = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=ATTENDANCE_STATUS_CHOICES,
        default='N',
    )
