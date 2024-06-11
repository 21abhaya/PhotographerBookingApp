from django.urls import path, include
from .views import *

app_name = "customer"

urlpatterns =[
    path('customer-create/', CustomerCreateView.asView, name='customer-create'),
    path('customers/', CustomerListView.asView, name='customer-create'),
    path('customer-detail/<str:pk>', CustomerDetailView.asView, name='customer-create'),
    path('customer-update/<str:pk>', CustomerUpdateView.asView, name='customer-create'),
    path('customer-delete/<str:pk>', CustomerDeleteView.asView, name='customer-create'),   
]