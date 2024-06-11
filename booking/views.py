from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import BookCall,BookASession

# BookCall CRUD

class BookCallCreateView(CreateView):
    model = BookCall
    # form_class =
    template_name = 'bookcall_create_update_view.html'
    success_url = reverse_lazy('booking:booked-calls-list')

class BookCallListView(ListView):
    model = BookCall
    # form_class = 
    context_object_name = 'bookedcalls'
    template_name = 'bookcall_list_view.html'
    paginate_by = 10

class BookCallDetailView(DetailView):
    model = BookCall
    context_object_name = 'bookedcall'
    template_name = 'bookcall_detail_view.html'

    
class BookCallUpdateView(UpdateView):
    model = BookCall
    # form_class =
    template_name = 'bookcall_create_update_view.html'
    success_url = reverse_lazy('booking:booked-calls-list')

class BookCallDeleteView(DeleteView):
    model = BookCall
    template_name = 'bookcall_delete_view.html'
    success_url = reverse_lazy('booking:booked-calls-list')

#BookASession CRUD

class BookASessionCreateView(CreateView):
    model = BookASession
    # form_class =
    template_name = 'bookasession_create_update_view.html'
    success_url = reverse_lazy('booking:booked-sessions-list')

class BookASessionListView(ListView):
    model = BookASession
    # form_class = 
    context_object_name = 'bookedsessions'
    template_name = 'bookasession_list_view.html'
    paginate_by = 10

class BookASessionDetailView(DetailView):
    model = BookASession
    context_object_name = 'bookedsession'
    template_name = 'bookasession_detail_view.html'

    
class BookASessionUpdateView(UpdateView):
    model = BookASession
    # form_class =
    template_name = 'bookasession_delete_view.html'
    success_url = reverse_lazy('booking:booked-sessions-list')

class BookASessionDeleteView(DeleteView):
    model = BookASession
    template_name = 'bookasession_delete_view.html'
    success_url = reverse_lazy('booking:booked-sessions-list')