from django import forms
from django.forms import ModelForm
from .models import Booked_appointments

class BookAppointment(ModelForm):  
    class Meta:
        model = Booked_appointments
        fields = '__all__'