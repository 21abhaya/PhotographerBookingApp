from django.urls import path, include
from .views import *

app_name = "booking"

urlpatterns =[
    path('call-booking-create/', BookCallCreateView.asView, name='call-booking-create'),
    path('booked-calls/', BookCallListView.asView, name='booked-calls-list'),
    path('booked-call-detail/<uuid:pk>', BookCallDetailView.asView, name='booked-call-detail'),
    path('booked-call-update/<uuid:pk>', BookCallUpdateView.asView, name='booked-call-update'),
    path('booked-call-delete/<uuid:pk>', BookCallDeleteView.asView, name='booked-call-delete'),
]

urlpatterns +=[
    path('session-booking-create/', BookASessionCreateView.asView, name='session-booking-create'),
    path('booked-sessions/', BookASessionListView.asView, name='booked-sessions-list'),
    path('booked-session-detail/<uuid:pk>', BookASessionDetailView.asView, name='booked-session-detail'),
    path('booked-session-update/<uuid:pk>', BookASessionUpdateView.asView, name='booked-session-update'),
    path('booked-session-delete/<uuid:pk>', BookASessionDeleteView.asView, name='booked-session-delete'),
]