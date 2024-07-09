from django.db import models


class Doctor(models.Model):
    SPECIALIZATIONS = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Oncologist', 'Oncologist'),
        ('Orthopedic', 'Orthopedic'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Urologist', 'Urologist'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Endocrinologist', 'Endocrinologist'),
        ('Pulmonologist', 'Pulmonologist'),
        ('Nephrologist', 'Nephrologist'),
        ('Hematologist', 'Hematologist'),
        ('Rheumatologist', 'Rheumatologist'),
        ('Infectious Disease Specialist', 'Infectious Disease Specialist'),
        ('General Practitioner', 'General Practitioner'),
        ('Surgeon', 'Surgeon'),
        ('Plastic Surgeon', 'Plastic Surgeon'),
        ('ENT Specialist', 'ENT Specialist'),  # Ear, Nose, and Throat
        ('Anesthesiologist', 'Anesthesiologist'),
        ('Radiologist', 'Radiologist'),
        ('Pathologist', 'Pathologist'),
        ('Allergist', 'Allergist'),
        ('Dermatopathologist', 'Dermatopathologist'),
        ('Immunologist', 'Immunologist'),
        ('Sports Medicine Specialist', 'Sports Medicine Specialist'),
        ('Palliative Care Specialist', 'Palliative Care Specialist'),
        ('Emergency Medicine Specialist', 'Emergency Medicine Specialist'),
    ]

    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    LOCATIONS = [
        ('Alzahra Hospital', 'Alzahra Hospital'),
        ('Kashani Hospital', 'Kashani Hospital'),
        ('Isa Ibn Maryam Hospital', 'Isa Ibn Maryam Hospital'),
        ('Chamran Hospital', 'Chamran Hospital'),
        ('Khanevadeh Hospital', 'Khanevadeh Hospital'),
        ('Khorshid Hospital', 'Khorshid Hospital'),
        ('Amin Hospital', 'Amin Hospital'),
        ('Private Clinic', 'Private Clinic'),
    ]

    TIME_CHOICES = [(f'{h:02d}:{m:02d}', f'{h:02d}:{m:02d}') for h in range(24) for m in (0, 30)]

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATIONS)
    location = models.CharField(max_length=50, choices=LOCATIONS)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    end_time = models.CharField(max_length=5, choices=TIME_CHOICES)

    def __str__(self):
        return self.name
