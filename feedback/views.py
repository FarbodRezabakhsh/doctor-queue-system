from django.shortcuts import render, redirect
from .models import Feedback
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required


@login_required
def give_feedback(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        feedback = Feedback(user=request.user, doctor=doctor, rating=rating, comment=comment)
        feedback.save()
        return redirect('feedback_confirm')
    return render(request, 'feedback/give_feedback.html', {'doctor': doctor})
