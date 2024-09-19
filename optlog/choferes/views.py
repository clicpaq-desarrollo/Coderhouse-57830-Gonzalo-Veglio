from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Chofer
from .forms import ChoferForm

class ChoferListView(LoginRequiredMixin,ListView):
    model = Chofer
    template_name = 'choferes/choferes_list.html'
    context_object_name = 'choferes'
    
class ChoferDetailView(LoginRequiredMixin,DetailView):
    model = Chofer
    template_name = 'choferes/chofer_detail.html'
    context_object_name = 'chofer'

class ChoferCreateView(LoginRequiredMixin,CreateView):
    model = Chofer
    form_class = ChoferForm
    template_name = 'choferes/chofer_form.html'
    success_url = reverse_lazy('choferes:choferes_list')

class ChoferUpdateView(LoginRequiredMixin,UpdateView):
    model = Chofer
    form_class = ChoferForm
    template_name = 'choferes/chofer_form.html'
    success_url = reverse_lazy('choferes:choferes_list')

class ChoferDeleteView(LoginRequiredMixin,DeleteView):
    model = Chofer 
    success_url = reverse_lazy('choferes:choferes_list')
