from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import datetime, time
from django.db import models
from doctors.models import Doctor

class Appointment(models.Model):
    TIME_CHOICES = [(time(h, m).strftime('%H:%M'), time(h, m).strftime('%H:%M')) for h in range(9, 17) for m in (0, 30) if not (h == 16 and m == 30)]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    is_reserved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor', 'date', 'time')

    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.date} at {self.time}"

    def clean(self):
        # Ensure doctor is set
        if not self.doctor:
            raise ValidationError("Appointment must have a doctor assigned.")

        # Convert time to datetime.time for comparison if it is not already
        if isinstance(self.time, str):
            appointment_time = datetime.strptime(self.time, '%H:%M').time()
        else:
            appointment_time = self.time

        # Convert doctor's start_time and end_time to datetime.time if they are strings
        if isinstance(self.doctor.start_time, str):
            doctor_start_time = datetime.strptime(self.doctor.start_time, '%H:%M').time()
        else:
            doctor_start_time = self.doctor.start_time

        if isinstance(self.doctor.end_time, str):
            doctor_end_time = datetime.strptime(self.doctor.end_time, '%H:%M').time()
        else:
            doctor_end_time = self.doctor.end_time

        # Check for overlapping appointments
        overlapping_appointments_exist = Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date,
            time=self.time,
            is_reserved=True
        ).exists()
        if overlapping_appointments_exist:
            raise ValidationError("This time slot is already booked for the selected doctor.")

        # Ensure the appointment time is within doctor's working hours
        if appointment_time < doctor_start_time or appointment_time >= doctor_end_time:
            raise ValidationError("Appointment time is outside the doctor's working hours.")
