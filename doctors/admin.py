from django.contrib import admin
from .models import Doctor, Specialization, AvailableTime

class AvailableTimeInline(admin.TabularInline):
    model = AvailableTime
    extra = 1

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'location']
    list_filter = ['specialization']
    search_fields = ['name', 'specialization__name', 'location']
    inlines = [AvailableTimeInline]

@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'day_of_week', 'start_time', 'end_time']
    list_filter = ['doctor', 'day_of_week']
    search_fields = ['doctor__name', 'day_of_week']
