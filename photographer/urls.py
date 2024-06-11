from django.urls import path, include
from .views import *

app_name = "photographer"

urlpatterns =[
    path('photographer-create/', PhotographerCreateView.as_view, name='photographer-create'),
    path('photographers/', PhotographerListView.as_view, name='photographers-list'),
    path('photographer-detail/<str:pk>', PhotographerDetailView.as_view, name='photographer-detail'),
    path('photographer-update/<str:pk>', PhotographerUpdateView.as_view, name='photographer-update'),
    path('photographer-delete/<str:pk>', PhotographerDeleteView.as_view, name='photographer-delete'),
]