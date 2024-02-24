from django.forms import ModelForm
from django import forms
from .models import Doctor_1_availability

class BookAppointment(ModelForm):    
    date = forms.TextInput()
    time = forms.TextInput()
    class Meta:
        model = Doctor_1_availability
        fields = ['date', 'time']