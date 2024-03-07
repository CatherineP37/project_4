from django.shortcuts import render, redirect
from django.views import generic
from .models import Availability
from .models import Booked_appointments
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import BookAppointment
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def account(request):
    print(request.user.is_authenticated)
    return render(request, 'account.html', {})

def appointments(request):
    return render(request, 'appointments.html', {})

def cancellation(request):
    return render(request, 'cancellation.html', {})

def close_account(request):
    return render(request, 'close_account.html', {})

def booking(request):
    context = {}
    form = BookAppointment()
    availability = Availability.objects.all()
    appointments = Booked_appointments.objects.all()

    context['availability'] = availability
    if request.method =='POST':        
        form = BookAppointment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.appointment = Availability.objects.get(id=request.POST["appointment"])
            instance.save()
            messages.success(request, 'You have booked the following appointment: ')
            return redirect('/')
        
    
    context['appointments'] = appointments

    context['form'] = form
    context['availability'] = Availability.objects.all()
    return render(request, 'booking.html', context)


 











