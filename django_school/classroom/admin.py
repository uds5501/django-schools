from django.contrib import admin
from .models import School,User,Subject,Quiz,Question,Answer,Student,TakenQuiz,StudentAnswer
# Register your models here.
admin.site.register(User)
admin.site.register(School)