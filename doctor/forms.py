from django import forms

from .models import Doctor
from accounts.models.users import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Doctor
        fields = ['name', 'resident']

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            phone_number=self.cleaned_data['phone_number']
        )
        user.save()
        doctor = super().save(commit=False)
        doctor.user = user
        if commit:
            doctor.save()
        return doctor
