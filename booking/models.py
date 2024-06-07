from django.db import models
from customer.models import Customer
from photographer.models import Photographer

import uuid

# Create your models here.

class BookBaseModel(models.Model):
    ticket = models.UUIDField(uuid)
    booking_made_on = models.DateTimeField(auto_now_add=True)
    
    

class BookCall(BookBaseModel):
    customer = models.OneToOneField(Customer, null=False, blank=False, on_delete=models.RESTRICT)
    photographer = models.OneToOneField(Photographer, null=False, blank=False, on_delete=models.RESTRICT)
    booked_for = models.DateTimeField()
    

class BookASession(BookBaseModel):
    customer = models.OneToOneField(Customer, null=False, blank=False, on_delete=models.RESTRICT)
    photographer = models.OneToOneField(Photographer, null=False, blank=False, on_delete=models.RESTRICT)
    booked_For = models.DateTimeField()

     
        
    
