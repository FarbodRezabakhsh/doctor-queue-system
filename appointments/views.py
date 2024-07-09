from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from appointments.forms import AppointmentForm
from django.core.exceptions import ValidationError

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = request.user

            try:
                appointment.clean()  # Ensure the appointment is valid
                appointment.save()
                return redirect('appointment_success')
            except ValidationError as e:
                form.add_error(None, e)
        else:
            print(form.errors)
    else:
        initial_data = {
            'doctor': doctor,
            'fee': doctor.fee,
            'location': doctor.location
        }
        form = AppointmentForm(initial=initial_data)

    return render(request, 'appointments/appointment_form.html', {'doctor': doctor, 'form': form})

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')