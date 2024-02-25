from django.shortcuts import render
from django.views import generic
from .models import Doctor_1_availability
from django.http import HttpResponse
from .forms import BookAppointment

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def account(request):
    print(request.user.is_authenticated)
    return render(request, 'account.html', {})

def appointments(request):
    return render(request, 'appointments.html', {})

def booking(request):
    return render(request, 'booking.html', {})

def cancellation(request):
    return render(request, 'cancellation.html', {})

def close_account(request):
    return render(request, 'close_account.html', {})

def doctor_1(request):   
    available_appointments = Doctor_1_availability.objects.all
    return render(request, 'doctor_1.html', {'available_appointments':available_appointments},)
    if request.method == "POST":        
        form = BookAppointment(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'doctor_1.html', {})
    else: 
        return render(request, 'doctor_1.html', {})

def doctors(request):
    form = BookAppointment
    return render(request, 'doctors.html', {'form':form})

def email_sent(request):
    return render(request, 'email_sent.html', {})








