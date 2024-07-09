import os
import django
import random
from datetime import time

# تنظیمات جنگو را بارگذاری کنید
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from doctors.models import Doctor

specializations = [
    "Cardiologist", "Dermatologist", "Endocrinologist", "Gastroenterologist",
    "Hematologist", "Neurologist", "Oncologist", "Ophthalmologist",
    "Orthopedic", "Pediatrician", "Psychiatrist", "Radiologist",
    "Surgeon", "Urologist", "General Practitioner", "Dentist",
    "Gynecologist", "Nephrologist", "Pulmonologist", "Rheumatologist"
]

locations = ["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Ahvaz", "Qom", "Kermanshah"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def create_doctors():
    for i in range(30):
        name = f"Doctor {i + 1}"
        specialization = random.choice(specializations)
        location = random.choice(locations)
        fees = {"consultation": random.randint(50000, 200000)}
        day_of_week = random.choice(days_of_week)
        start_time = time(random.randint(8, 10), random.choice([0, 15, 30, 45]))
        end_time = time(random.randint(16, 18), random.choice([0, 15, 30, 45]))

        doctor = Doctor(
            name=name,
            specialization=specialization,
            location=location,
            fees=fees,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time
        )
        doctor.save()


if __name__ == '__main__':
    create_doctors()
    print("30 doctors have been created.")
