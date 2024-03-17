from django.contrib import admin
from .models import Booked_appointments, Availability


# Register your models here.
admin.site.register(Booked_appointments)
admin.site.register(Availability)

