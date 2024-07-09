from django.db import models
from django.conf import settings
from doctors.models import Doctor
from django.core.exceptions import ValidationError


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
        # Check for overlapping appointments
        overlapping_appointments = Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date,
            time=self.time
        ).exists()
        if overlapping_appointments:
            raise ValidationError("This time slot is already booked for the selected doctor.")

        # Ensure the appointment time is within doctor's working hours
        if self.time < self.doctor.start_time or self.time > self.doctor.end_time:
            raise ValidationError("Appointment time is outside the doctor's working hours.")


