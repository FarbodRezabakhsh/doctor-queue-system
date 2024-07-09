from django import forms
from appointments.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor', 'fee', 'location']  # شامل تمامی فیلدهای مورد نیاز

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['doctor'].widget.attrs['readonly'] = True
        self.fields['fee'].widget.attrs['readonly'] = True
        self.fields['location'].widget.attrs['readonly'] = True
