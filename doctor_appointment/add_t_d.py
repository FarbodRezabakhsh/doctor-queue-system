import os
import django
import random
from datetime import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from doctors.models import Doctor, Specialization, AvailableTime

specializations = Specialization.objects.all()
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
start_times = [time(9, 0), time(10, 0), time(11, 0), time(13, 0), time(14, 0), time(15, 0)]
end_times = [time(10, 0), time(11, 0), time(12, 0), time(14, 0), time(15, 0), time(16, 0)]

for i in range(30):
    name = f'Dr. Doctor {i + 1}'
    specialization = random.choice(specializations)
    location = random.choice(locations)

    doctor = Doctor.objects.create(name=name, specialization=specialization, location=location)

    for day in days_of_week:
        start_time = random.choice(start_times)
        end_time = random.choice(end_times)
        while end_time <= start_time:
            end_time = random.choice(end_times)

        AvailableTime.objects.create(doctor=doctor, day_of_week=day, start_time=start_time, end_time=end_time)

print("30 doctors and their available times added to the database.")
