from django.contrib import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin, AccessMixin

from .models import Customer
from .forms import CustomerForm
# Create your views here.

class CustomerCreateView(CreateView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create_update_view.html'
    success_url = reverse_lazy('customer:customers-list')

    def test_func(self):
        return self.request.user.has_perm('customer.add_customer')
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to add customers.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class CustomerListView(ListView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer_list_view.html'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to view customers' list.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CustomerDetailView(DetailView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Customer
    context_object_name = 'customer'
    template_name = 'customer_detail_view.html'

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to view customer details.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


    
class CustomerUpdateView(UpdateView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create_update_view.html'
    success_url = reverse_lazy('customer:customers-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.has_perm('customer.update_customer')
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to update customer information.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CustomerDeleteView(DeleteView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Customer
    template_name = 'customer_delete_view.html'
    success_url = reverse_lazy('customer:customers-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.has_perm('customer.delete_customer')
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to delete customer information.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


    
