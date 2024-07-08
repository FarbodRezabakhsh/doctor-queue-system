from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from .models import Appointment
from datetime import datetime


@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)

    if request.method == 'POST':
        # Process the booking
        selected_fee = request.POST.get('fee')
        selected_date = request.POST.get('date')
        selected_time = request.POST.get('time')

        if selected_fee not in doctor.fees.values():
            return render(request, 'appointments/appointment_form.html', {
                'doctor': doctor,
                'error_message': 'Invalid fee selected.',
            })

        # Create the appointment
        appointment = Appointment.objects.create(
            doctor=doctor,
            patient=request.user,
            date=datetime.strptime(selected_date, '%Y-%m-%d').date(),
            time=datetime.strptime(selected_time, '%H:%M').time(),
            fee=selected_fee
        )

        return redirect('appointment_success')

    return render(request, 'appointments/appointment_form.html', {'doctor': doctor})


def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')
