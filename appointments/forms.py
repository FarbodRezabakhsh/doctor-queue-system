from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor', 'fee', 'location']  # include time instead of selected_time

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['time'].widget = forms.HiddenInput()  # Hidden field for time
        self.fields['doctor'].widget.attrs['readonly'] = True
        self.fields['fee'].widget.attrs['readonly'] = True
        self.fields['location'].widget.attrs['readonly'] = True
