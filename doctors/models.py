from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=255, default="Unknown")  # Add default value
    fees = models.JSONField(default=dict)
    day_of_week = models.CharField(max_length=10)  # e.g., 'Monday', 'Tuesday', etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
