from django.contrib import admin
from booking.models import BookBaseModel, BookCall, BookASession
# Register your models here.

admin.site.register(BookBaseModel)
admin.site.register(BookCall)
admin.site.register(BookASession)
