from django.db import models

# Create your models here.
class Exam(models.Model):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
    academicyear = models.ForeignKey('schools.AcademicYear', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    # exam_type = models.CharField(max_length=255, blank=True)
    exam_class = models.SmallIntegerField() # standard
    exam_date = models.DateTimeField()
    is_grade = models.BooleanField(default=False)
    results_published = models.BooleanField(default=False)

class SubjectMarkConf(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey('classroom.Subject', on_delete=models.CASCADE)
    max_mark = models.IntegerField(default=0)
    pass_mark = models.IntegerField(default=0)

class Marks(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey('classroom.Subject', on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    # ce =  models.IntegerField(default=0, blank=True, null=True)
    # theory = models.IntegerField(default=0, blank=True, null=True)
    # practical = models.IntegerField(default=0, blank=True, null=True)
    mark = models.IntegerField(default=0, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True)
    

# class Exam(models.Model):
#   name = models.CharField(max_length=255)
#     # classroom = models.ForeignKey('classroom.ClassRoom', on_delete=models.CASCADE)
#     academicyear = models.ForeignKey('schools.AcademicYear', on_delete=models.CASCADE)
#     exam_type = models.CharField(max_length=255, blank=True)
#     exam_class = models.SmallIntegerField() # standard
#     exam_date = models.DateTimeField()
#     mark_types = models.ManyToManyField('MarkType')
#     # results_published = models.BooleanField(default=False)

# class MarkType(models.Model):
#   """
#   eg: Theory, Continous Evaluation, Practial, Internal etc
#   """
#   name = models.CharField(max_length=255)
#   description = models.CharField(max_length=255)

# class SubjectMaxMarks(models.Model):
#   exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#   mark_type = models.ForeignKey(MarkType, on_delete=models.CASCADE)
#   subject = models.ForeignKey('classroom.Subject', on_delete=models.CASCADE)

# class Marks(models.Model):
#   exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#   subject = models.ForeignKey('classroom.Subject', on_delete=models.CASCADE)
#   student = models.ForeignKey('students,Student', on_delete=models.CASCADE)
#   mark_type = models.ForeignKey(MarkType, on_delete=models.CASCADE)


# # VIDHYADHAN MODELS
# class Exam(BaseModel):
#     exam_name = models.CharField(max_length=255, null=True)
#     exam_class = models.CharField(max_length=255, null=True)
#     academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE, related_name='Exam', null=True)
#     exam_type = models.CharField(max_length=255, blank=True, null=True)
#     gradesystem = models.ForeignKey('academics.GradingSystem', on_delete=models.CASCADE, null=True)
#     status = models.SmallIntegerField(default = 1)

# class MarkEntry(BaseModel):
#     class_name = models.ForeignKey('academics.Classes', on_delete=models.CASCADE, null=True)
#     exam_name = models.ForeignKey('academics.Exam', on_delete=models.CASCADE, related_name='exams', null=True)
    

# class StudentMarkEnter(BaseModel):
#     markentry = models.ForeignKey('academics.MarkEntry', on_delete=models.CASCADE, null=True)
#     student = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, null=True)
#     subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE, null=True)
#     mark_grade = models.CharField(max_length=255)
# ###################################

# class StudentCourse(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

# class Marks(models.Model):
#     studentcourse = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, choices=test_name, default='Internal test 1')
#     marks1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])