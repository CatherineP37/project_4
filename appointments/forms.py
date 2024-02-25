from django import forms
from django.forms import ModelForm
from .models import Doctor_1_availability

class BookAppointment(ModelForm):  
    class Meta:
        model = Doctor_1_availability
        fields = ('date', 'time')