from django.contrib import admin
from .models import PatientModel

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username','phone','image')
    def username(self,obj):
        return obj.user.username
    
admin.site.register(PatientModel,PatientAdmin)