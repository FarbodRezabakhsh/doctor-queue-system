from django.db import models
from django.contrib.auth.models import User
from accounts.models.users import *

# Create your models this.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    resident = models.CharField(max_length=100)
    info_text = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_time = models.DateTimeField()
    location_text = models.CharField(max_length=250)
    visit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user} will be visited at {self.visit_time} '

class WorkTable(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_table = models.JSONField()
    visit_price = models.DecimalField(max_digits=10, decimal_places=2)

class PatientInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    medical_history = models.TextField()
    drug_history = models.TextField()
