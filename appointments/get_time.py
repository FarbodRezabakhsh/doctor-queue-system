from datetime import datetime, timedelta
from .models import Appointment


def get_available_times(doctor, date):
    available_times = set()  # Using a set to avoid duplicates
    start_time = datetime.strptime(doctor.start_time, '%H:%M')
    end_time = datetime.strptime(doctor.end_time, '%H:%M')
    current_time = start_time

    while current_time < end_time:
        available_times.add(current_time.strftime('%H:%M'))
        current_time += timedelta(minutes=30)  # assuming appointments are 30 minutes long

    # Remove already booked times
    booked_times = Appointment.objects.filter(doctor=doctor, date=date).values_list('time', flat=True)
    booked_times = set(booked_times)  # Ensure booked times are also in set

    available_times = available_times - booked_times

    return sorted(available_times)
