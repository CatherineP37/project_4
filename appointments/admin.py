from django.contrib import admin
from .models import Patient, Appointment, Doctor_1_availability, Doctor_2_availability, Doctor_3_availability, Doctor_4_availability, Doctor_5_availability, Doctor_6_availability

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Doctor_1_availability)
admin.site.register(Doctor_2_availability)
admin.site.register(Doctor_3_availability)
admin.site.register(Doctor_4_availability)
admin.site.register(Doctor_5_availability)
admin.site.register(Doctor_6_availability)
