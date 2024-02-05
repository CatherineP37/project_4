from . import views
from django.urls import path

urlpatterns = [
    path('', view.PatientsList.as_view(), name='home'),
]
