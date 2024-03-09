from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('account/',views.account, name="account"),  
    path('booking/', views.booking, name="booking"),
    path('cancellation/<str:pk>/', views.cancellation, name="cancellation"),   
    path('close_account/', views.close_account, name="close_account"),  
    path('booked_appointment/', views.booked_appointment, name="booked_appointment"),
   # path('double_booked/', views.double_booked, name="double_booked"),
]
