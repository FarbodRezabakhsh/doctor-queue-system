from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))


# Profile Model
class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Foreign key relation with User model
    name = models.CharField(max_length=250)  # First name of the user
    phone_number = models.CharField(max_length=11)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    create_date = models.DateTimeField(
        auto_now_add=True
    )  # Date and time when profile was created
    update_date = models.DateTimeField(
        auto_now=True
    )  # Date and time when profile was last updated

    def __str__(self):
        return self.user.email


# Signal to create profile when user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Wallet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Foreign key relation with User model
    balance = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'Wallet of {self.user} (Balance: {self.balance})'