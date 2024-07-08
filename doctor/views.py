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
from django.contrib.auth import authenticate, login, logout
from .models import Doctor
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from django.db.models import Q

# Create your views here.


class DoctorHomeView(ListView):
    model = Doctor
    template_name = 'doctor/home.html'
    context_object_name = 'doctors'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(resident__icontains=query)
            )
        return queryset

class RegisterDoctorView(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request,'doctor/register.html',{'form':form})

    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor:doctor_home')
        return render(request,'doctor/register.html',{'form':form})


class LoginDoctorView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'doctor/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor:doctor_home')
        return render(request, 'doctor/login.html', {'form': form})

class LogoutDoctorView(View):
    def get(self, request):
        logout(request)
        return redirect('doctor:doctor_home')