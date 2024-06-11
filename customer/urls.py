from django.urls import path, include
from .views import *

app_name = "customer"

urlpatterns =[
    path('customer-create/', CustomerCreateView.as_view, name='customer-create'),
    path('customers/', CustomerListView.as_view, name='customer-list'),
    path('customer-detail/<str:pk>', CustomerDetailView.as_view, name='customer-detail'),
    path('customer-update/<str:pk>', CustomerUpdateView.as_view, name='customer-update'),
    path('customer-delete/<str:pk>', CustomerDeleteView.as_view, name='customer-delete'),   
]