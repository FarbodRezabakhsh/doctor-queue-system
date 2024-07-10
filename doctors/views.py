from django.db.models import Q
from django.shortcuts import render
from .models import Doctor
from .forms import SearchForm


def doctor_detail(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})


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
