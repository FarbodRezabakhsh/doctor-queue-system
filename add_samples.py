import os
import django
import random
from django.core.exceptions import ValidationError
from faker import Faker
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from doctors.models import Doctor
from appointments.models import Appointment
from feedback.models import Feedback

fake = Faker()

# Ensure you have correct choices for Doctor model fields
specializations = [choice[0] for choice in Doctor.SPECIALIZATIONS]
locations = [choice[0] for choice in Doctor.LOCATIONS]
days_of_week = [choice[0] for choice in Doctor.DAYS_OF_WEEK]
time_choices = Appointment.TIME_CHOICES

User = get_user_model()

# Create 30 random doctors
for _ in range(30):
    name = fake.name()
    specialization = random.choice(specializations)
    location = random.choice(locations)
    fee = round(random.uniform(50, 500), 2)
    day_of_week = random.choice(days_of_week)
    start_time = '09:00'
    end_time = '16:00'

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
    print(f"Doctor {name} created successfully.")

# Create 10 random users
if User.objects.count() == 0:
    print("No users found in the database. Creating sample users...")
    for _ in range(10):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123',
            phone_number=fake.phone_number(),
            wallet_balance=round(random.uniform(100, 1000), 2)
        )
        user.save()
    print("Sample users created successfully.")

# Create appointments for doctors
for doctor in Doctor.objects.all():
    for _ in range(random.randint(5, 10)):  # Create between 5 to 10 appointments for each doctor
        patient = random.choice(User.objects.all())

        # Ensure the appointment date is on the doctor's working day
        appointment_date = fake.date_between(start_date='-1y', end_date='today')
        while appointment_date.strftime('%A') != doctor.day_of_week:
            appointment_date = fake.date_between(start_date='-1y', end_date='today')

        # Generate appointment times within doctor's working hours
        doctor_start_time = datetime.strptime(doctor.start_time, '%H:%M').time()
        doctor_end_time = datetime.strptime(doctor.end_time, '%H:%M').time()

        available_times = []
        current_time = datetime.combine(appointment_date, doctor_start_time)
        end_time = datetime.combine(appointment_date, doctor_end_time)
        while current_time + timedelta(minutes=30) <= end_time:
            available_times.append(current_time.time())
            current_time += timedelta(minutes=30)

        if not available_times:
            continue

        appointment_time = random.choice(available_times)

        appointment = Appointment(
            doctor=doctor,
            patient=patient,
            date=appointment_date,
            time=appointment_time.strftime('%H:%M'),
            fee=doctor.fee,
            location=doctor.location,
            is_reserved=True  # Mark the appointment as reserved
        )

        try:
            appointment.clean()
            appointment.save()
            print(f"Appointment for {doctor.name} on {appointment_date} at {appointment_time} created successfully.")
        except ValidationError as e:
            print(f"Failed to create appointment for {doctor.name}: {e}")

# Create feedbacks for doctors
for doctor in Doctor.objects.all():
    for user in User.objects.all():
        rating = random.randint(1, 5)
        comment = fake.paragraph(nb_sentences=3)
        feedback = Feedback(user=user, doctor=doctor, rating=rating, comment=comment)
        feedback.save()
        print(f"Feedback from {user.username} for {doctor.name} created successfully.")

print("Doctors, users, appointments, and feedback created successfully.")
