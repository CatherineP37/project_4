from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('account/',views.account, name="account"),    
    path('appointments/',views.appointments, name="appointments"),
 #   path('booking/', views.booking, name="booking"),
    path('cancellation/', views.cancellation, name="cancellation"),   
    path('close_account/', views.close_account, name="close_account"),  
    path('email_sent/', views.email_sent, name="email_sent"),   
]
