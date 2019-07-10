from django.db import models
from schools.models import School
from django.conf import settings
# Create your models here.

class ClassRoom(models.Model):
    # Class for exampl: 8A, 7B, 10I etc
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    #teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    # i don't know whether the below things are required or not
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    #students = models.ManyToManyField(User, related_name="course_students",blank=True)

    class Meta:
        unique_together = ("school", "name")
    
    def __str__(self):
        return self.name

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

    def __str__(self):
        # return f"{self.classroom.name} - {self.subject} on {self.DAY_CHOICES[self.dayoftheweek][1]} {self.starttime}"
        return "{0} - {1} on {2} {3}".format(self.classroom.name, self.subject, self.DAY_CHOICES[self.dayoftheweek][1], self.starttime)
