from django.db import models
from customer.models import Customer
from photographer_booking_app.app.models import Photographer

import uuid

# Create your models here.

class BookBaseModel(models.Model):
    ticket = models.UUIDField(uuid)
    booking_made_on = models.DateTimeField(auto_now_add=True)
    
    

class BookCall(BookBaseModel):
    customer = models.OneToOneField(Customer, null=False, blank=False)
    photographer = models.OneToOneField(Photographer, null=False, blank=False)
    booked_for = models.DateTimeField()
    

class BookASession(BookBaseModel):
    customer = models.OneToOneField(Customer, null=False, blank=False)
    photographer = models.OneToOneField(Photographer, null=False, blank=False)
    booked_For = models.DateTimeField()

     
        
    
