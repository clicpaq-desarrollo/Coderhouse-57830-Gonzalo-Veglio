from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Envio, ProductoEnvio, Producto
from .forms import EnvioForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
 

from django.http import JsonResponse
from .models import Producto
  

def productos_cliente(request, cliente_id):
    productos = Producto.objects.filter(cliente_id=cliente_id)  
    print(productos)  
    productos_data = [{'id': producto.id, 'nombre': producto.nombre} for producto in productos]
    return JsonResponse(productos_data, safe=False)



def productos_por_cliente(request):
    cliente_id = request.GET.get('cliente_id')
    
    if cliente_id:
        productos = Producto.objects.filter(cliente_id=cliente_id).values('id', 'nombre')
        return JsonResponse(list(productos), safe=False)
    
    return JsonResponse([], safe=False)


class EnvioListView(LoginRequiredMixin, ListView):
    model = Envio
    template_name = 'envios/envios_list.html'
    context_object_name = 'envios'  
    
    def get_queryset(self):
        query = self.request.GET.get('q') 
        queryset = super().get_queryset() 

        if query:
            queryset = queryset.filter(
                Q(guia__icontains=query) | 
                Q(cliente__nombre__icontains=query) | 
                Q(destinatario_nombre__icontains=query) 
            )

        return queryset
    
    
 
    
class EnvioDeleteView(LoginRequiredMixin, DeleteView):
    model = Envio 
    success_url = reverse_lazy('envios:envios_list')

   
class EnvioDetailView(LoginRequiredMixin, DetailView):
    model = Envio
    template_name = 'envios/envio_detail.html'
    context_object_name = 'envio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = self.object.productos.all()

        total_bultos = productos.count()
        total_peso = sum(producto.peso for producto in productos)
        total_volumen = sum(producto.volumen for producto in productos)

        context['productos'] = productos
        context['total_bultos'] = total_bultos
        context['total_peso'] = total_peso
        context['total_volumen'] = total_volumen
        return context
    
class EnvioBuscarDetailView( DetailView):
    model = Envio
    template_name = 'envios/detalle_envio.html'
    context_object_name = 'envio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = self.object.productos.all()

        total_bultos = productos.count()
        total_peso = sum(producto.peso for producto in productos)
        total_volumen = sum(producto.volumen for producto in productos)

        context['productos'] = productos
        context['total_bultos'] = total_bultos
        context['total_peso'] = total_peso
        context['total_volumen'] = total_volumen
        return context
    
class EnvioCreateView(LoginRequiredMixin, CreateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envios:envios_list')

    def form_valid(self, form):
        envio = form.save()  # Guarda el envío primero
        productos_ids = self.request.POST.getlist('productos')  # Obtener todos los productos seleccionados

        # Limpiar productos previamente asociados (aunque no debería haber ninguno al crear)
        envio.productos.clear()

        for producto_id in productos_ids:
            if producto_id:  # Verifica que el ID no esté vacío
                producto = get_object_or_404(Producto, id=producto_id)
                envio.productos.add(producto)  # Agregar el producto al envío

        return super().form_valid(form)


class EnvioUpdateView(LoginRequiredMixin, UpdateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envios:envios_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        context['productos_seleccionados'] = self.object.productos.values_list('id', flat=True)
        return context

    def form_valid(self, form):
        envio = form.save()
        
        # Obtener los IDs de los productos seleccionados
        productos_ids = self.request.POST.getlist('productos')
        print("Productos seleccionados:", productos_ids)  # Debugging

        # Limpiar los productos previamente asociados
        envio.productos.clear()

        # Agregar los nuevos productos seleccionados
        for producto_id in productos_ids:
            if producto_id:
                producto = get_object_or_404(Producto, id=producto_id)
                envio.productos.add(producto)

        return super().form_valid(form)

    