from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .models import Doctor,PatientInfo,Appointment,WorkTable
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
from django.shortcuts import get_object_or_404

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
                Q(name__contains=query) | Q(resident__contains=query)
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


class DoctorDetailView(View):
    def get(self, request,id):
        doctor = get_object_or_404(Doctor,pk=id)
        work_table = get_object_or_404(WorkTable,doctor=doctor)
        return render(request,'doctor/doctor_detail.html',{'doctor':doctor,'work_table':work_table})

class BookAppointmentView(LoginRequiredMixin, View):
    def post(self, request, doctor_id):
        doctor = get_object_or_404(Doctor, id=doctor_id)
        visit_time = request.POST.get('visit_time')
        location = request.POST.get('location')
        price = request.POST.get('price')

        Appointment.objects.create(
            doctor=doctor,
            user=request.user,
            visit_time=visit_time,
            location_text=location,
            visit_price=price,
        )
        return redirect('doctor:doctor_detail', id=doctor_id)
















