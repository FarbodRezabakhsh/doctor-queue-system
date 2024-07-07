from django.shortcuts import render, redirect
from .models import Appointment
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required


@login_required
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        time = request.POST['time']
        fee = doctor.fee
        appointment = Appointment(user=request.user, doctor=doctor, time=time, fee=fee)
        appointment.save()
        # Send confirmation email logic here
        return redirect('appointment_confirm')
    return render(request, 'appointments/book_appointment.html', {'doctor': doctor})
