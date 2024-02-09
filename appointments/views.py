from django.shortcuts import render
from django.views import generic
from .models import Patients
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def account(request):
    return render(request, 'account.html', {})

def appointments(request):
    return render(request, 'appointments.html', {})

def booking(request):
    return render(request, 'booking.html', {})

def cancellation(request):
    return render(request, 'cancellation.html', {})

def change_password(request):
    return render(request, 'change_password.html', {})

def close_account(request):
    return render(request, 'close_account.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def doctor_1(request):
    return render(request, 'doctor_1.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def email_sent(request):
    return render(request, 'email_sent.html', {})

def login(request):
    return render(request, 'login.html', {})

def lost_password(request):
    return render(request, 'lost_password.html', {})

def past_appointments(request):
    return render(request, 'past_appointments.html', {})

def sign_up(request):
    return render(request, 'sign_up.html', {})




