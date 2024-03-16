from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Availability
from .models import Booked_appointments
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import BookAppointment
from django.contrib import messages
from datetime import date

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def account(request):
    print(request.user.is_authenticated)
    return render(request, 'account.html', {})

def cancellation(request, pk):
    booking = Booked_appointments.objects.get(id=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('account')
    context = {'booking':booking}
    return render(request, 'cancellation.html', context)


def booking(request):    
    context = {}
    form = BookAppointment()
    availability = Availability.objects.all()
    appointments = Booked_appointments.objects.all()

    # Retrieve the IDs of already booked appointments
    booked_ids = [appointment.appointment.id for appointment in appointments]
    print(booked_ids)

    # Filter out booked appointments from availability
    availability1 = availability.exclude(id__in=booked_ids)
    print(availability1)

    context['availability'] = availability1
    print(context)
    if request.method =='POST':       
        form = BookAppointment(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.appointment = Availability.objects.get(id=request.POST["appointment"])         
            instance.save()            
            return redirect('booked_appointment')
            
    context['appointments'] = appointments
    context['form'] = form
    context['availability'] = availability1
    return render(request, 'booking.html', context)

def booked_appointment(request):
    user = request.user
    print('USER: ', user)
    appointments = Booked_appointments.objects.filter(user=user) 
    print('APP: ', appointments)
   
    return render(request, 'booked_appointment.html', {
        'user':user,
        'appointments':appointments, 
        'booking':booking,
    })

def double_booked(request):
    return render(request, 'double_booked.html', {})

def update_booking(request, pk):
    appointment = get_object_or_404(Booked_appointments, id=pk)
    if request.method == 'POST':
        form = BookAppointment(request.POST, instance=appointment)
        if form.is_valid():
            updated_appointment = form.save(commit=False)
            updated_appointment.user = request.user
            updated_appointment.appointment = Availability.objects.get(id=request.POST.get("appointment"))
            updated_appointment.save()
            messages.success(request, 'Your appointment has been updated successfully.')
            return redirect('account')  
    else:
        form = BookAppointment(instance=appointment)
    context = {
        'form': form,
        'availability': Availability.objects.all()        
    }
    return render(request, 'update_booking.html', context)   

def check_date(appointment):
    now = datetime.datetime.now()
    appointment = Event.objects.get(date=date)

    if appointment.date < now: 
        appointment.delete()




 











