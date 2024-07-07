from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    available_times = models.TextField()  # This can be a JSONField for more complex scheduling
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
