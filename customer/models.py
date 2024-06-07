from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Customer(models.Model):

    """Customer model defines a customer entity""" 


    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254, blank=False, null=False)
    Phone_Number = PhoneNumberField(max_length = 15, null=False, blank=False, verbose_name='Phone')


    def __str__(self):
        """String for representing the model object."""
        return f'{self.first_name} {self.last_name}' 
