from django import forms
from django.forms import ModelForm
from .models import Booked_appointments

class BookAppointment(ModelForm):  
    class Meta:
        model = Booked_appointments
        fields = ('first_name', 'last_name', 'email_address', 'phone_number', 'date', 'time')