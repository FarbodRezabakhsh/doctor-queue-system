from django.db import models
from accounts.models import User
from doctor.models import Doctor


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='doctor_comment', on_delete=models.CASCADE)
    content = models.TextField()
    approach = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} comments in {self.doctor}'


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='doctor_rate', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} rating to {self.doctor}'
