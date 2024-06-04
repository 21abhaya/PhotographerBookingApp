from django.db import models

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    about = models.TextField()
    display_picture = models.ImageField()