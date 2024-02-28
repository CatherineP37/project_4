from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Patient(models.Model):
    patient_id_number = models.IntegerField()
    first_name = models.CharField()
    last_name = models.CharField()
    email_address = models.EmailField()
    postal_address = models.CharField()
    phone_number = models.IntegerField()


class Appointment(models.Model):
    appointment_id = models.IntegerField()
    patient_id_number = models.OneToOneField(
    Patient, on_delete=models.CASCADE)
    doctor_id_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Availability(models.Model):    
    date = models.DateField()
    time = models.TimeField()


