from django.contrib import admin

# Register your models here.
from .models import School,User,Subject
# Register your models here.
admin.site.register(User)
admin.site.register(School)
admin.site.register(Subject)