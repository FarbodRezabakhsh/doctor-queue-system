from django.db import models

# Create your models this.


class Doctor(models.Model):
    doctor = models.CharField(max_length=255)

    def __str__(self):
        return self.doctor