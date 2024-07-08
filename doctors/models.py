from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, default="Unknown")  # Add default value
    fees = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class AvailableTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='available_times')
    day_of_week = models.CharField(max_length=10)  # e.g., 'Monday', 'Tuesday', etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week} {self.start_time}-{self.end_time}"
