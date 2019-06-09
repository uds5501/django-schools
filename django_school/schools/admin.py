from django.contrib import admin
from .models import School,User,ClassRoom

# Register your models here.
admin.site.register(User)
admin.site.register(School)
admin.site.register(ClassRoom)