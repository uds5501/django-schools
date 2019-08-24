from django.db import models

# IT AT SCHOOL
# #########################
class BasicInfo(models.Model):
    establish_date = models.CharField(max_length=30)
    area = models.CharField(max_length=50)
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
    designation = models.CharField(max_length=200)
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
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    date_of_join = models.DateField()

    def __str__(self):
        return self.name

## END of IT @ school models
#########################################


from django.contrib.auth.models import AbstractUser

# class Location(models.Model):
#     address_1 = models.CharField(max_length=50, blank= True)
#     address_2 = models.CharField(max_length=50, blank=True)
#     city = models.CharField(max_length=50)
#     district = models.CharField(max_length=50)
#     state_province = models.CharField(max_length=20, default='kerala')
#     zip_postal_code = models.CharField(max_length=10, blank=True)
#     country = models.CharField(max_length=20, default='india')

#     def __str__(self):
#         return self.city    

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
    # location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    
    @property
    def is_student(self):
        "Is the user a student?"
        return self.user_type == 1

    @property
    def is_teacher(self):
        "Is the user a teacher?"
        return self.user_type == 2    

class Event(models.Model):
    '''This model stores Event.'''
    startdatetime = models.DateTimeField()
    enddatetime = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class AcademicYear(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
# class Period(models.Model):
#     # A Period will just be a recurring Event(every week) related to a Classroom.
    
#     classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
#     starttime = models.TimeField()
#     endtime = models.TimeField()
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)

#     DAY_CHOICES = (
#         (0, 'Monday'),
#         (1, 'Tuesday'),
#         (2, 'Wednesday'),
#         (3, 'Thursday'),
#         (4, 'Friday'),
#         (5, 'Saturday'),
#         (6, 'Sunday'),
#     )
#     dayoftheweek = models.IntegerField(choices=DAY_CHOICES)

#     def __str__(self):
#         # return f"{self.classroom.name} - {self.subject} on {self.DAY_CHOICES[self.dayoftheweek][1]} {self.starttime}"
#         return "{0} - {1} on {2} {3}".format(self.classroom.name, self.subject, self.DAY_CHOICES[self.dayoftheweek][1], self.starttime)


