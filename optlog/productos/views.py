from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm
from django.db.models import Q


class ProductoDeleteView(LoginRequiredMixin,DeleteView):
    model = Producto 
    success_url = reverse_lazy('productos:productos_list')

from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/productos_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset()

        if query:
            # Filtrar por nombre de producto o por cliente
            queryset = queryset.filter(
                Q(nombre__icontains=query) | 
                Q(cliente__nombre__icontains=query)
            )

        return queryset


class ProductoDetailView(LoginRequiredMixin,DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'
    
class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:productos_list')
    
class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:productos_list')