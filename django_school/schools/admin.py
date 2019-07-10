from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import School, BasicInfo #User,ClassRoom, Period, BasicInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', )

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(School)
admin.site.register(BasicInfo)
# admin.site.register(ClassRoom)
# admin.site.register(Period)
