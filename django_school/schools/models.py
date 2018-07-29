from django.db import models

# IT AT SCHOOL
# #########################
class BasicInfo(models.Model):
    establish_date = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    rooms = models.IntegerField(blank =True, null = True)
    teaching_staffs = models.IntegerField(blank =True, null = True)
    non_teaching_staffs = models.IntegerField(blank =True, null = True)

class School(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    district = models.CharField(max_length=30)
    edu_district = models.CharField(max_length=30)
    sub_district = models.CharField(max_length=30)
    url_id = models.IntegerField(blank =True, null = True)
    basic_info = models.ForeignKey(BasicInfo,on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    
    # staff_strength = models.ForeignKey(StaffStrength,on_delete=models.CASCADE,null=True)
    #staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class StaffStrength(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='staffstrength')
    year = models.CharField(max_length =30)
    designation = models.CharField(max_length=50)
    strength = models.IntegerField(blank =True, null = True)

class StudentStrength(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='studentstrength')
    course = models.IntegerField()
    strength = models.IntegerField(blank =True, null = True)
    sampoorna = models.IntegerField(blank =True, null = True)
    available_uid = models.IntegerField(blank =True, null = True)
    valid_uid = models.IntegerField(blank =True, null = True)
    partialy_match_uid = models.IntegerField(blank =True, null = True)
    invalid_uid = models.IntegerField(blank =True, null = True)
    none = models.IntegerField(blank =True,null = True)
    
class Staff(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='staffs')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    date_of_join = models.DateField()

    def __str__(self):
        return self.name

## END of IT @ school models
#########################################


from django.contrib.auth.models import AbstractUser

class Location(models.Model):
    address_1 = models.CharField(max_length=50, blank= True)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state_province = models.CharField(max_length=20, default='kerala')
    zip_postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=20, default='india')

    def __str__(self):
        return self.city    

    #def get_absolute_url(self):
    #    return reverse('location_detail', args=[str(self.id)])

class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'secretary'),
      (4, 'supervisor'),
      (5, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=1)
    school = models.ForeignKey(School,on_delete=models.CASCADE, related_name='users',null=True,blank=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    
    @property
    def is_student(self):
        "Is the user a student?"
        return self.user_type == 1

    @property
    def is_teacher(self):
        "Is the user a teacher?"
        return self.user_type == 2    

class Course(models.Model):
    # Class for exampl: 8A, 7B, 10I etc
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    #teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    # i don't know whether the below things are required or not
    teachers = models.ManyToManyField(User, related_name="course_teachers",blank=True)
    students = models.ManyToManyField(User, related_name="course_students",blank=True)

    
    class Meta:
        unique_together = ("school", "name")
    
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('course_detail', args=[str(self.id)])

from django.utils import timezone
class Session(models.Model):
    #This will be replaced by Event model in the school_calendar app.
    #A Session will just be a recurring Event related to a Course.
    
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="sessions")
    startdatetime = models.DateTimeField()
    enddatetime = models.DateTimeField()

    def __str__(self):
        startdatetime = timezone.localtime(self.startdatetime)
        return self.course.name + " on " + startdatetime.strftime("%A, %B %d at %X")

    # def get_absolute_url(self):
    #    return reverse('session_detail', args=[str(self.id)])

class Event(models.Model):
    '''This model stores Event.'''
    startdatetime = models.DateTimeField()
    enddatetime = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=255)
    school = models.ForeignKey(School,on_delete=models.CASCADE)