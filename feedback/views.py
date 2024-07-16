from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from .models import Doctor, Feedback
from django.core.mail import send_mail
from django.template.loader import render_to_string

@login_required
def give_feedback(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    user_appointments = Appointment.objects.filter(user=request.user, doctor=doctor).exists()

    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']

        if comment and not user_appointments:
            # اگر کاربر نوبت نداشته باشد و نظر بخواهد ثبت کند
            error_message = "شما نمی‌توانید نظر بدهید زیرا نوبتی نزد این پزشک نداشته‌اید."
            return render(request, 'feedback/give_feedback.html', {'doctor': doctor, 'error_message': error_message})

        # بررسی وجود بازخورد قبلی
        existing_feedback = Feedback.objects.filter(user=request.user, doctor=doctor).first()
        if existing_feedback:
            existing_feedback.rating = rating
            existing_feedback.comment = comment if user_appointments else existing_feedback.comment
            existing_feedback.save()
        else:
            new_feedback = Feedback(user=request.user, doctor=doctor, rating=rating, comment=comment if user_appointments else '')
            new_feedback.save()

        # ارسال ایمیل تأیید
        send_confirmation_email(request.user, doctor, rating, comment)

        return redirect('feedback_confirm', doctor_id=doctor_id)

    return render(request, 'feedback/give_feedback.html', {'doctor': doctor})

def send_confirmation_email(user, doctor, rating, comment):
    stars = '★' * int(rating) + '☆' * (5 - int(rating))
    subject = 'تأیید نظر و امتیاز شما'
    context = {
        'user': user,
        'doctor': doctor,
        'rating': stars,
        'comment': comment,
    }
    message = render_to_string('emails/feedback_confirmation.html', context)
    send_mail(subject, '', 'your-email@example.com', [user.email], html_message=message)


@login_required
def feedback_confirm(request, doctor_id):
    feedback = get_object_or_404(Feedback, doctor_id=doctor_id, user=request.user)
    return render(request, 'feedback/feedback_confirm.html', {'feedback': feedback})
