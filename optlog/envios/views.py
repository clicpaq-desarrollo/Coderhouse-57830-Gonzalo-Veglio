from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Envio
from .forms import EnvioForm
from django.db.models import Q 

class EnvioListView(LoginRequiredMixin,ListView):
    model = Envio
    template_name = 'envios/envios_list.html'
    context_object_name = 'envio'
    
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
    
# class EnvioDetailView(DetailView):
#     model = Envio
#     template_name = 'envios/detalle_envio.html'
#     context_object_name = 'envio' 
    

class EnvioDetailView(LoginRequiredMixin,DetailView):
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
    
class EnvioCreateView(LoginRequiredMixin,CreateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envios:envios_list')
    
class EnvioUpdateView(LoginRequiredMixin,UpdateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envios:envios_list')
    
class EnvioDeleteView(LoginRequiredMixin,DeleteView):
    model = Envio 
    success_url = reverse_lazy('envios:envios_list')
    

