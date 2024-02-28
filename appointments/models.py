from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Booked_appointments(models.Model):   
    first_name = models.CharField()
    last_name = models.CharField()
    email_address = models.EmailField()  
    phone_number = models.IntegerField()

class Availability(models.Model):    
    date = models.DateField()
    time = models.TimeField()


