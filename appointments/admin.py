from django.contrib import admin
from .models import Patients, Appointments, Doctor_1_availability

# Register your models here.
admin.site.register(Patients)
admin.site.register(Appointments)
admin.site.register(Doctor_1_availability)
