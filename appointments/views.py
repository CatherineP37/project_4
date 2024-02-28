from django.shortcuts import render
from django.views import generic
from .models import Availability
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import BookAppointment

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
    available_appointments = Availability.objects.all
    return render(request, 'booking.html, {'available_appointments':available_appointments},)
    submitted = False
    if request.method == "POST":
        form = BookAppointment(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/booking?submitted=True')
    else:
        form = BookAppointment
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'booking.html', {'form':form, 'submitted':submitted})
 


def email_sent(request):
    return render(request, 'email_sent.html', {})








