from django.db import models
from django.conf import settings
from doctors.models import Doctor
from django.core.exceptions import ValidationError
from datetime import datetime

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)

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
            try:
                appointment_time = datetime.strptime(self.time, '%H:%M:%S').time()
            except ValueError:
                appointment_time = datetime.strptime(self.time, '%H:%M').time()
        else:
            appointment_time = self.time

        # Convert doctor's start_time and end_time to datetime.time if they are strings
        if isinstance(self.doctor.start_time, str):
            try:
                doctor_start_time = datetime.strptime(self.doctor.start_time, '%H:%M:%S').time()
            except ValueError:
                doctor_start_time = datetime.strptime(self.doctor.start_time, '%H:%M').time()
        else:
            doctor_start_time = self.doctor.start_time

        if isinstance(self.doctor.end_time, str):
            try:
                doctor_end_time = datetime.strptime(self.doctor.end_time, '%H:%M:%S').time()
            except ValueError:
                doctor_end_time = datetime.strptime(self.doctor.end_time, '%H:%M').time()
        else:
            doctor_end_time = self.doctor.end_time

        # Check for overlapping appointments
        overlapping_appointments_exist = Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date,
            time=self.time
        ).exists()
        if overlapping_appointments_exist:
            raise ValidationError("This time slot is already booked for the selected doctor.")

        # Ensure the appointment time is within doctor's working hours
        if appointment_time < doctor_start_time or appointment_time > doctor_end_time:
            raise ValidationError("Appointment time is outside the doctor's working hours.")
