from django.contrib import admin
from .models import RawData


admin.site.site_header='Admin'


class RawDataAdmin(admin.ModelAdmin):
    list_display=('Patient_ID','Consultant','Specialization','Disease','Complexity')
admin.site.register(RawData,RawDataAdmin)

