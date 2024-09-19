from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

from django.http import JsonResponse
from miscelaneas.models import Localidad

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = 'clientes/clientes_list.html'
    context_object_name = 'clientes'


class ClienteDetailView(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'


class ClienteCreateView(LoginRequiredMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('clientes:clientes_list')


class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('clientes:clientes_list')


class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente 
    success_url = reverse_lazy('clientes:clientes_list')
    
    
 