from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'Null'))


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class Wallet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Foreign key relation with User model
    balance = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'Wallet of {self.user} (Balance: {self.balance})'


# Signal to create profile when user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Signal to create wallet when user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)




