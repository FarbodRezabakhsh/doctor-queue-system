from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'location', 'fee', 'day_of_week', 'start_time', 'end_time']
    list_filter = ['name', 'specialization', 'location', 'fee', 'day_of_week', 'start_time', 'end_time']
    search_fields = ['name', 'specialization', 'location', 'fee', 'day_of_week', 'start_time', 'end_time']

