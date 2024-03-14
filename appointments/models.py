from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models.signals import post_save

# Create your models here

class Availability(models.Model):    
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

 

class Booked_appointments(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    email_address = models.EmailField(null=True)  
    phone_number = models.IntegerField(null=True)
    appointment = models.ForeignKey(Availability, null=True, on_delete= models.CASCADE)
    
    def __str__(self):
        username = self.user.username if self.user else 'Unknown user'      
        return f"{username} appointment: {str(self.appointment)}"

    
  

   
        







