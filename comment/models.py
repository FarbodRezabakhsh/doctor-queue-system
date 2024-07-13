from django.db import models
from django.utils import timezone
from accounts.models.users import User
from doctor.models import Doctor

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='doctor_comments')
    comment = models.TextField()
    