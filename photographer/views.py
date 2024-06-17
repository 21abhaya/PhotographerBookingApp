from django.contrib import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin, AccessMixin

from .models import Photographer
from .forms import PhotographerForm
# Create your views here.

class PhotographerCreateView(CreateView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Photographer
    form_class = PhotographerForm
    template_name = 'photographer_create_update_view.html'
    success_url = reverse_lazy('photographer:photographers-list')

    def test_func(self):
        return self.request.user.has_perm('photographer.add_photographer')
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to add Photographers.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class PhotographerListView(ListView):
    model = Photographer
    context_object_name = 'photographers'
    template_name = 'photographer_list_view.html'
    paginate_by = 10

class PhotographerDetailView(DetailView):
    model = Photographer
    context_object_name = 'photographer'
    template_name = 'photographer_detail_view.html'
    
class PhotographerUpdateView(UpdateView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Photographer
    form_class = PhotographerForm
    template_name = 'photographer_create_update_view.html'
    success_url = reverse_lazy('photographer:photographers-list')

    def test_func(self):
        return self.request.user.has_perm('photographer.update_photographer')
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to update Photographers.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class PhotographerDeleteView(DeleteView, UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin):
    model = Photographer
    template_name = 'photographer_delete_view.html'
    success_url = reverse_lazy('photographer:photographers-list')
    
    def test_func(self):
        return self.request.user.has_perm('photographer.delete_photographer')
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You do not have permission to delete Photographers.",
            )
            return render(self.request, HttpResponseRedirect)
        return super().handle_no_permission()
    
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)