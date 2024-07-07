from django.contrib import admin
from .models import Doctor,User,PatientInfo,Appointment,WorkTable

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('name','resident')
    ordering = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('doctor','user','location_text','visit_price')
    ordering = ('visit_time',)


@admin.register(WorkTable)
class WorkTableAdmin(admin.ModelAdmin):
    list_display=('doctor','time_table')
    ordering = ('time_table',)

@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ('user','weight','height')