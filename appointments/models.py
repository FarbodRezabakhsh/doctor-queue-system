from django.db import models
from django.conf import settings
from doctors.models import Doctor
from datetime import time


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default='sunday')
    time = models.TimeField(default=time(10, 0))
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.date} at {self.time}"
