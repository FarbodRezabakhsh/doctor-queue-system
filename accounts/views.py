from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserLoginForm, CustomUserForm
# Create your views here.


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "email", "password"
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("doctor:doctor_home")


class CustomRegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = CustomUserForm

    def get_success_url(self):
        print('hi')
        return reverse_lazy('accounts:login')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("doctor:home")
            # Redirect to the task list page if user is already authenticated
        return super(CustomRegisterView, self).get(*args, **kwargs)