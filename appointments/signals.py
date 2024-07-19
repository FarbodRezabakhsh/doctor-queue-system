from django.dispatch import Signal
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import Appointment


appointment_booked = Signal()

@receiver(appointment_booked)
def send_appointment_email(sender, user, doctor, appointment, **kwargs):
    mail_subject = 'Confirm Appointment'
    message = render_to_string('registration/appointment_confirmation_email_for_doctor.html', {
        'user': user,
        'doctor': doctor,
        'appointment': appointment,
    })
    email = EmailMessage(mail_subject, message, to=[user.email, doctor.email])
    email.content_subtype = 'html'  # Set the content type to HTML
    email.send()