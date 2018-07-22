from django.contrib import admin
from .models import School,User,Course

# Register your models here.
admin.site.register(User)
admin.site.register(School)
admin.site.register(Course)