from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from doctors.forms import SearchForm
from doctors.models import Doctor
from appointments.models import Appointment
from feedback.models import Feedback


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date', 'time')
    doctor_feedback = Feedback.objects.filter(doctor=doctor).order_by('-id')

    return render(request, 'doctors/doctor_detail.html', {
        'doctor': doctor,
        'appointments': appointments,
        'doctor_feedback': doctor_feedback,
    })


def doctor_list(request):
    query = None
    results = []
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Doctor.objects.filter(
                Q(name__icontains=query) |
                Q(specialization__icontains=query)
            )

    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html',
                  {'doctors': doctors, 'form': form, 'query': query, 'results': results})


def show_feedback(request, doctor_id):
    doctor_feedback = Feedback.objects.get(doctor=doctor_id)
    return render(request, 'doctors/doctor_detail.html', {'doctor_feedback': doctor_feedback})
