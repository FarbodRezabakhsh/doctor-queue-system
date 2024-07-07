from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile
from django.core.exceptions import ValidationError


# User Login Form
class UserLoginForm(forms.Form):
    email = forms.CharField()  # Email field for user authentication
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # Password field for user authentication

    def get_user(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if '@' in email and email and password:
            user = authenticate(email=email, password=password)
            return user
        elif email and password:
            try:
                user_id = User.objects.get(phone_number=email)
            except User.DoesNotExist:
                return None
            email = user_id.email
            user = authenticate(email=email, password=password)
            return user
        return None

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleand_data = super().clean()
        user = self.get_user()
        if user is None:
            raise forms.ValidationError("User or password is wrong")
        elif not user.is_active:
            raise forms.ValidationError("user is not active")
        return cleand_data


# User Registration Form
class CustomUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="password", widget=forms.PasswordInput
    )  # Password field for user registration
    password2 = forms.CharField(
        label="confirm password", widget=forms.PasswordInput
    )  # Confirm password field for user registration

    class Meta:
        model = User
        fields = ("email", "phone_number")

    # Method to validate password confirmation
    def clean_password2(self):
        cd = self.cleaned_data
        if (
            cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]
        ):
            raise ValidationError("passwords don't match")
        return cd["password2"]

    # Method to validate email uniqueness
    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This email already exists")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError("This phone number already exists")
        return phone_number

    # Method to save user registration form
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


