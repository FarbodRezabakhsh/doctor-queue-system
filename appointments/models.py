from django.db import models
from users.models import CustomUser
from doctors.models import Doctor


class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.DateTimeField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    confirmation_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.doctor} at {self.time}'
