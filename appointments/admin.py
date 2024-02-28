from django.contrib import admin
from .models import Patient, Appointment, Doctor_1_availability, Doctor_2_availability, Doctor_3_availability, Doctor_4_availability, Doctor_5_availability, Doctor_6_availability

# Register your models here.
admin.site.register(Booked_appointments)
admin.site.register(Availability)

