from django.shortcuts import render
from django.views import generic
from .models import Patients
from django.http import HttpResponse

# Create your views here.


class PatientsList(generic.ListView):
    queryset = Patients.objects.all()
    template_name = "appointments/index.html"
    paginate_by = 6
