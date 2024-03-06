from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Availability(models.Model):    
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

class Booked_appointments(models.Model):   
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    email_address = models.EmailField(null=True)  
    phone_number = models.IntegerField(null=True)
    appointment = models.ForeignKey(Availability, null=True, on_delete= models.CASCADE)
    




