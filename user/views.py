from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserLoginForm, UserCreationForm
# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "user/login.html"
    fields = "email", "password"
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("doctor:home")


class CustomRegisterView(CreateView):
    template_name = "user/register.html"