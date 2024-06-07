from django.db import models
from customer.models import Customer
from photographer_booking_app.app.models import Photographer

import uuid

# Create your models here.

class BookBaseModel(models.Model):
    Ticket = models.UUIDField
    
    

class BookCall(BookBaseModel):
    Customer = models.OneToOneField(Customer, null=False, blank=False)
    Photographer = models.OneToOneField(Photographer, null=False, blank=False)
    Booking_Date_Time = models.DateTimeField()
    

class BookaSession(BookBaseModel):
    Customer = models.OneToOneField(Customer, null=False, blank=False)
    Photographer = models.OneToOneField(Photographer, null=False, blank=False)
    Booking_Date_Time = models.DateTimeField()
     
        
    
