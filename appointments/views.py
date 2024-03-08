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

def cancellation(request, pk):
    booking = Booked_appointments.objects.get(id=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('appointments')
    context = {'booking':booking}
    return render(request, 'cancellation.html', context)

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
            return redirect('booked_appointment')
        
    
    context['appointments'] = appointments

    context['form'] = form
    context['availability'] = Availability.objects.all()
    return render(request, 'booking.html', context)

def booked_appointment(request):
    user = request.user
    print('USER: ', user)
    appointments = Booked_appointments.objects.filter(user=user) 
    print('APP: ', appointments)
    # print('BOOKING: ', appointments.)
    # booking = Booked_appointments.appointment.objects.filter(user=request.user)   
    return render(request, 'booked_appointment.html', {
        'user':user,
        'appointments':appointments, 
        'booking':booking,
    })




 











