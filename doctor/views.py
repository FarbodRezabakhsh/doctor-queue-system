from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .models import Doctor,PatientInfo,Appointment,User,WorkTable
from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,FormView,View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from .models import Doctor
from django.contrib.auth import login, logout

# Create your views here.


class DoctorHomeView(ListView):
    model = Doctor
    template_name = 'doctor/home.html'
    context_object_name = 'doctors'

class RegisterDoctorView(CreateView):
    form_class = UserCreationForm
    template_name = 'doctor/register.html'
    success_url = reverse_lazy('doctor_home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class LoginDoctorView(LoginView):
    template_name = 'doctor/login.html'

    def get_success_url(self):
        return reverse_lazy('doctor_home')

class LogoutDoctorView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('doctor_login')