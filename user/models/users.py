from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user.models.managers import UserManager


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True
    )  # Email field for user authentication
    phone_number = models.CharField(max_length=11)
    is_staff = models.BooleanField(
        default=False
    )  # Boolean field to indicate if user is staff or not
    is_active = models.BooleanField(
        default=True
    )  # Boolean field to indicate if user is active or not
    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['phone_number',]  # Required fields for user registration
    USERNAME_FIELD = "email"  # Field to use for user authentication
    PHONE_NUMBER_FIELD = "phone_number"  # Field to use for user authentication using phone number.
    create_date = models.DateTimeField(
        auto_now_add=True
    )  # Date and time when user was created
    update_date = models.DateTimeField(
        auto_now=True
    )  # Date and time when user was last updated

    objects = UserManager()  # Manager for user model

    def __str__(self):
        return self.email
