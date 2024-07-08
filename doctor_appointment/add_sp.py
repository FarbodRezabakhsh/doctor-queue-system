import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from doctors.models import Specialization

specializations = [
    'Cardiology', 'Dermatology', 'Neurology', 'Pediatrics', 'Radiology',
    'Oncology', 'Orthopedics', 'Gastroenterology', 'Endocrinology', 'Ophthalmology',
    'Anesthesiology', 'Psychiatry', 'Surgery', 'Urology', 'Gynecology',
    'Pulmonology', 'Nephrology', 'Rheumatology', 'Hematology', 'Allergy & Immunology',
    'Geriatrics', 'Pathology', 'Emergency Medicine', 'Family Medicine', 'Internal Medicine',
    'Otolaryngology', 'Plastic Surgery', 'Infectious Disease', 'Sports Medicine', 'Dentistry'
]

for specialization in specializations:
    Specialization.objects.get_or_create(name=specialization)

print("Specializations added to the database.")
