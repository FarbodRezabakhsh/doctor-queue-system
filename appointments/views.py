from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from doctors.models import Doctor
from .forms import AppointmentForm
from .get_time import get_available_times
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


def send_appointment_email(user, doctor, appointment):
    mail_subject = 'تأیید نوبت'
    message = render_to_string('registration/appointment_confirmation_email.html', {
        'user': user,
        'doctor': doctor,
        'appointment': appointment,
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.content_subtype = 'html'  # تنظیم نوع محتوای ایمیل به HTML
    email.send()

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    user = request.user

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = user

            if not appointment.time:
                form.add_error('time', 'لطفاً زمان نوبت خود را انتخاب کنید.')
            elif user.wallet_balance < doctor.fee:
                form.add_error(None, 'موجودی کیف پول شما برای رزرو این نوبت کافی نیست.')
            else:
                try:
                    appointment.clean()
                    appointment.save()
                    user.wallet_balance -= doctor.fee
                    user.save()
                    send_appointment_email(user, doctor, appointment)  # ارسال ایمیل
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

    today = datetime.today().date()
    next_appointment_day = None
    available_times = []
    for i in range(15):
        appointment_date = today + timedelta(days=i)
        if appointment_date.strftime('%A') == doctor.day_of_week:
            next_appointment_day = appointment_date
            available_times = get_available_times(doctor, next_appointment_day)
            break

    return render(request, 'appointments/appointment_form.html', {
        'doctor': doctor,
        'form': form,
        'available_times': available_times,
        'next_appointment_day': next_appointment_day
    })


def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')
