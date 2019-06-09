from django.contrib import admin
from .models import School,User,ClassRoom, Period

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', )

admin.site.register(User, UserAdmin)
admin.site.register(School)
admin.site.register(ClassRoom)
admin.site.register(Period)