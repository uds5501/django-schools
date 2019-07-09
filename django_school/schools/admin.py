from django.contrib import admin
# from .models import School,User,ClassRoom #, Period
from django.contrib.auth import get_user_model

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', )

admin.site.register(get_user_model(), UserAdmin)
# admin.site.register(School)
# admin.site.register(ClassRoom)
# admin.site.register(Period)