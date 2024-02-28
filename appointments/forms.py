from django import forms
from django.forms import ModelForm
from .models import Availability

class BookAppointment(ModelForm):  
    class Meta:
        model = Availability
        fields = ('date', 'time')