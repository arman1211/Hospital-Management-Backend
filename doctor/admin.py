from django.contrib import admin
from .models import Specialization,Designation,AvailableTime,DoctorModel,ReviewModel

# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','fee','image')

    def name(self,obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(AvailableTime)
admin.site.register(DoctorModel,DoctorAdmin)
admin.site.register(ReviewModel)
