from models import Availability, Booked_appointments

# Signal
def delete_appointment(sender, instance, created, **kwargs):
                
    if created:
        Availability.objects.delete(instance)
        print("Is it working?")    

    post_save.connect(delete_appointment, sender=Booked_appointments)
