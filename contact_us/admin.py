from django.contrib import admin
from .models import ContactModel

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone','problem')
        
admin.site.register(ContactModel,ContactAdmin)