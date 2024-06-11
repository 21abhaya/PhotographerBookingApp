from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Photographer

# Create your views here.

class PhotographerCreateView(CreateView):
    model = Photographer
    # form_class =
    template_name = 'photographer_create_update_view.html'
    success_url = reverse_lazy('photographer:photographers-list')

class PhotographerListView(ListView):
    model = Photographer
    # form_class = 
    context_object_name = 'photographers'
    template_name = 'photographer_list_view.html'
    paginate_by = 10

class PhotographerDetailView(DetailView):
    model = Photographer
    context_object_name = 'photographer'
    template_name = 'photographer_detail_view.html'

    
class PhotographerUpdateView(UpdateView):
    model = Photographer
    # form_class =
    template_name = 'photographer_delete_view.html'
    success_url = reverse_lazy('photographer:photographers-list')

class PhotographerDeleteView(DeleteView):
    model = Photographer
    template_name = 'photographer_delete_view.html'
    success_url = reverse_lazy('photographer:photographers-list')
