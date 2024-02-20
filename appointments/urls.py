from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('account.html', views.account, name="account"),
    path('appointments.html', views.appointments, name="appointments"),
    path('booking.html', views.booking, name="booking"),
    path('cancellation.html', views.cancellation, name="cancellation"),   
    path('close_account.html', views.close_account, name="close_account"),    
    path('doctor_1.html', views.doctor_1, name="doctor_1"),
    path('doctors.html', views.doctors, name="doctors"),
    path('email_sent.html', views.email_sent, name="email_sent"), 


]
