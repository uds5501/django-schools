from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    school = models.ForeignKey(School,on_delete=models.CASCADE, related_name='users',null=True)

from django.utils.html import escape, mark_safe
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)