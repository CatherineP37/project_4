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
