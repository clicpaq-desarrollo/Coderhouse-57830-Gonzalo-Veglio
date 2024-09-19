from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

class ProductoDeleteView(LoginRequiredMixin,DeleteView):
    model = Producto 
    success_url = reverse_lazy('productos:productos_list')

class ProductoListView(LoginRequiredMixin,ListView):
    model = Producto
    template_name = 'productos/productos_list.html'
    context_object_name = 'productos'

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