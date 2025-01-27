from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from .models import Doctor, Feedback
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

@login_required
def give_feedback(request, doctor_id):
    print(request.user)
    doctor = get_object_or_404(Doctor, id=doctor_id)
    user_appointments = Appointment.objects.filter(patient=request.user, doctor=doctor).exists()

    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']

        if comment and not user_appointments:
            # if we dont have appointment information from this user
            error_message = "You can't comment for every physician that you don't have appointment"
            print(user_appointments)
            return render(request, 'feedback/give_feedback.html', {'doctor': doctor, 'error_message': error_message})

        # check history of feedback
        existing_feedback = Feedback.objects.filter(user=request.user, doctor=doctor).first()
        if existing_feedback:
            existing_feedback.rating = rating
            existing_feedback.comment = comment if user_appointments else existing_feedback.comment
            existing_feedback.save()
        else:
            new_feedback = Feedback(user=request.user, doctor=doctor, rating=rating, comment=comment if user_appointments else '')
            new_feedback.save()

        # send confirm email contain this feedback
        send_confirmation_email(request.user, doctor, rating, comment)

        return redirect('feedback_confirm', doctor_id=doctor_id)

    return render(request, 'feedback/give_feedback.html', {'doctor': doctor})

def send_confirmation_email(user, doctor, rating, comment):
    stars = '★' * int(rating) + '☆' * (5 - int(rating))
    subject = f'Your feedback for {doctor.name} has been submitted'
    context = {
        'user': user,
        'doctor': doctor,
        'rating': stars,
        'comment': comment,
    }
    message = render_to_string('feedback/feedback_confirmation.html', context)
    email = EmailMessage(subject, message, to=[user.email])
    email.content_subtype = 'html'  # Set the email content type to HTML
    email.send()

@login_required
def feedback_confirm(request, doctor_id):
    feedback = get_object_or_404(Feedback, doctor_id=doctor_id, user=request.user)
    return render(request, 'feedback/feedback_confirm.html', {'feedback': feedback})
