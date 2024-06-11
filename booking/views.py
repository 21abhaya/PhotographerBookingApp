from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import BookCall,BookASession

# BookCall CRUD

class BookCallCreateView(CreateView):
    model = BookCall
    # form_class =
    template_name = 'bookCall_create_update_view.html'
    success_url = reverse_lazy('booking:bookedCalls-list')

class BookCallListView(ListView):
    model = BookCall
    # form_class = 
    context_object_name = 'BookedCalls'
    template_name = 'BookCall_list_view.html'
    paginate_by = 10

class BookCallDetailView(DetailView):
    model = BookCall
    context_object_name = 'BookedCall'
    template_name = 'BookCall_detail_view.html'

    
class BookCallUpdateView(UpdateView):
    model = BookCall
    # form_class =
    template_name = 'BookCall_delete_view.html'
    success_url = reverse_lazy('BookCall:BookCalls-list')

class BookCallDeleteView(DeleteView):
    model = BookCall
    template_name = 'BookCall_delete_view.html'
    success_url = reverse_lazy('BookCall:BookedCalls-list')

#BookASession CRUD

class BookASessionCreateView(CreateView):
    model = BookASession
    # form_class =
    template_name = 'BookASession_create_update_view.html'
    success_url = reverse_lazy('BookASession:BookedSessions-list')

class BookASessionListView(ListView):
    model = BookASession
    # form_class = 
    context_object_name = 'BookASession'
    template_name = 'BookASession_list_view.html'
    paginate_by = 10

class BookASessionDetailView(DetailView):
    model = BookASession
    context_object_name = 'BookASession'
    template_name = 'BookASession_detail_view.html'

    
class BookASessionUpdateView(UpdateView):
    model = BookASession
    # form_class =
    template_name = 'BookASession_delete_view.html'
    success_url = reverse_lazy('BookASession:BookCalls-list')

class BookASessionDeleteView(DeleteView):
    model = BookASession
    template_name = 'BookASession_delete_view.html'
    success_url = reverse_lazy('booking:BookCalls-list')