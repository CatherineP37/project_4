from django.shortcuts import render
from django.views import generic
from .models import Patients
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

