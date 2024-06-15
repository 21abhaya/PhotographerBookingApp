from django.urls import path, include
from .views import *

app_name = "booking"

urlpatterns =[
    path('call-booking-create/', BookCallCreateView.as_view(), name='call-booking-create'),
    path('booked-calls/', BookCallListView.as_view(), name='booked-calls-list'),
    path('booked-call-detail/<uuid:pk>', BookCallDetailView.as_view(), name='booked-call-detail'),
    path('booked-call-update/<uuid:pk>', BookCallUpdateView.as_view(), name='booked-call-update'),
    path('booked-call-delete/<uuid:pk>', BookCallDeleteView.as_view(), name='booked-call-delete'),
]

urlpatterns +=[
    path('session-booking-create/', BookASessionCreateView.as_view(), name='session-booking-create'),
    path('booked-sessions/', BookASessionListView.as_view(), name='booked-sessions-list'),
    path('booked-session-detail/<uuid:pk>', BookASessionDetailView.as_view(), name='booked-session-detail'),
    path('booked-session-update/<uuid:pk>', BookASessionUpdateView.as_view(), name='booked-session-update'),
    path('booked-session-delete/<uuid:pk>', BookASessionDeleteView.as_view(), name='booked-session-delete'),
]