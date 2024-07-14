from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required

@login_required
def give_feedback(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']

        # Check if the feedback already exists for the user and doctor
        existing_feedback = Feedback.objects.filter(user=request.user, doctor=doctor).first()
        if existing_feedback:
            existing_feedback.rating = rating
            existing_feedback.comment = comment
            existing_feedback.save()
        else:
            new_feedback = Feedback(user=request.user, doctor=doctor, rating=rating, comment=comment)
            new_feedback.save()

        return redirect('feedback_confirm', doctor_id=doctor_id)

    return render(request, 'feedback/give_feedback.html', {'doctor': doctor})

@login_required
def feedback_confirm(request, doctor_id):
    feedback = get_object_or_404(Feedback, doctor_id=doctor_id, user=request.user)
    return render(request, 'feedback/feedback_confirm.html', {'feedback': feedback})
