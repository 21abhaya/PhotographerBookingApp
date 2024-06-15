from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Customer
from .forms import CustomerForm
# Create your views here.

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create_update_view.html'
    success_url = reverse_lazy('customer:customers-list')

class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer_list_view.html'
    paginate_by = 10

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'customer_detail_view.html'

    
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create_update_view.html'
    success_url = reverse_lazy('customer:customers-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete_view.html'
    success_url = reverse_lazy('customer:customers-list')
