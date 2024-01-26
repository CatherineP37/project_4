from django.contrib import admin
from .models import Patients, Appointments, Doctor_1_availability, Doctor_2_availability, Doctor_3_availability

# Register your models here.
admin.site.register(Patients)
admin.site.register(Appointments)
admin.site.register(Doctor_1_availability)
admin.site.register(Doctor_2_availability)
admin.site.register(Doctor_3_availability)
