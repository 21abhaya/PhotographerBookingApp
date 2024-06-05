from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from config.settings.base import MEDIA_URL



class Photographer(models.Model):

    """Photographer model defines a photographer entity"""


    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254, blank=False, null=False)
    about = models.TextField(verbose_name="Who am I?", blank=False, null=False)
    display_picture = models.ImageField(upload_to="photographer/display_pictures/", default='/photographer/display_pictures/default.jpg')
    Phone_Number = PhoneNumberField(max_length = 15, null=False, blank=False, verbose_name='Phone')
    Fees = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name='Fees/hour')
    #Portfolio = models.ForeignKey('Portfolio', on_delete=models.RESTRICT, blank=False, null=False)
    #Category = models.ForeignKey('Category', on_delete=models.RESTRICT, null=False, blank=False)


    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return f"{MEDIA_URL}/photographer/display_pictures/default.jpg"
        
    def __str__(self):
        """String for representing the model object."""
        return f'{self.first_name} {self.last_name}' 
    

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
    

