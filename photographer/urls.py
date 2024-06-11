from django.urls import path, include
from .views import *

app_name = "photographer"

urlpatterns =[
    path('photographer-create/', views.PhotographerCreateView.asView, name='photographer-create'),
    path('photographer-list/', views.PhotographerListView.asView, name='photographers'),
    path('photographer-detail/<str:pk>', views.PhotographerDetailView.asView, name='photographer-detail'),
    path('photographer-update/<str:pk>', views.PhotographerUpdateView.asView, name='photographer-update'),
    path('photographer-delete/<str:pk>', views.PhotographerdeleteView.asView, name='photographer-delete'),
]