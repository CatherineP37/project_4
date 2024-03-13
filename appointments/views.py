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

    context['availability'] = availability
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
    context['availability'] = Availability.objects.all()
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

def delete_appointment(request, pk):
   
    appointment_instance = get_object_or_404(Booked_appointments, id=pk)

    if appointment_instance.is_past_date:
        action = 'delete record of'
    else:
        action = 'cancel'

        context = {
            'appointment_instance': appointment_instance,
            'action': action,
        }
        return render(request, 'delete_appointment.html', context)




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
            return redirect('account')  # Or wherever you want to redirect after updating
    else:
        form = BookAppointment(instance=appointment)
    context = {
        'form': form,
        'availability': Availability.objects.all()
    }
    return render(request, 'update_booking.html', context)   

{% comment %}  

#def check_date(booking):
    #booking = Booked_appointments.objects.get(date=date, time=time)
    #now = datetime.datetime.now()

    #if booking.date < now: 
        #booking.delete()

{% endcomment %}


 











