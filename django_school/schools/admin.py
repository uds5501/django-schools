from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import School, BasicInfo, AcademicYear #User,ClassRoom, Period, BasicInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', )

class AcademicYearAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.status:
            # deactivate all other academic years
            active_items = AcademicYear.objects.filter(status=True).update(status = False)
        super().save_model(request, obj, form, change)

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(School)
admin.site.register(BasicInfo)
admin.site.register(AcademicYear, AcademicYearAdmin)
# admin.site.register(ClassRoom)
# admin.site.register(Period)
