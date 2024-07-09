import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from doctors.models import Doctor

fake = Faker()

specializations = [choice[0] for choice in Doctor.SPECIALIZATIONS]
locations = [choice[0] for choice in Doctor.LOCATIONS]
days_of_week = [choice[0] for choice in Doctor.DAYS_OF_WEEK]
time_choices = [choice[0] for choice in Doctor.TIME_CHOICES]

# ایجاد 50 دکتر تصادفی
for _ in range(50):
    name = fake.name()
    specialization = random.choice(specializations)
    location = random.choice(locations)
    fee = round(random.uniform(50, 500), 2)
    day_of_week = random.choice(days_of_week)
    start_time = random.choice(time_choices)
    end_time = random.choice(time_choices)

    while start_time >= end_time:
        start_time = random.choice(time_choices)
        end_time = random.choice(time_choices)

    doctor = Doctor(
        name=name,
        specialization=specialization,
        location=location,
        fee=fee,
        day_of_week=day_of_week,
        start_time=start_time,
        end_time=end_time
    )

    doctor.save()

print("50 random doctors created successfully.")
