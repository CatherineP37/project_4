from django.contrib import admin
from .models import Patients, Appointments

# Register your models here.
admin.site.register(Patients)
admin.site.register(Appointments)
