from django.urls import path, include
from .views import *

app_name = "photographer"

urlpatterns =[
    path('photographer-create/', PhotographerCreateView.asView, name='photographer-create'),
    path('photographers/', PhotographerListView.asView, name='photographers-list'),
    path('photographer-detail/<str:pk>', PhotographerDetailView.asView, name='photographer-detail'),
    path('photographer-update/<str:pk>', PhotographerUpdateView.asView, name='photographer-update'),
    path('photographer-delete/<str:pk>', PhotographerDeleteView.asView, name='photographer-delete'),
]