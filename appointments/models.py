from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Patients(models.Model):
    patient_id_number = models.IntegerField()
    first_name = models.CharField()
    last_name = models.CharField()
    email_address = models.EmailField()
    postal_address = models.CharField()
    phone_number = models.IntegerField()


class Appointments(models.Model):
    appointment_id = models.IntegerField()
    patient_id_number = models.OneToOneField(
        Patients, on_delete=models.CASCADE)
    doctor_id_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Doctor_1_availability(models.Model):
    appointment_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Doctor_2_availability(models.Model):
    appointment_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Doctor_3_availability(models.Model):
    appointment_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Doctor_4_availability(models.Model):
    appointment_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Doctor_5_availability(models.Model):
    appointment_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
