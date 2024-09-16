from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Envio
from .forms import EnvioForm

class EnvioListView(ListView):
    model = Envio
    template_name = 'envios/envios_list.html'
    context_object_name = 'envio'

class EnvioDetailView(DetailView):
    model = Envio
    template_name = 'envios/envio_detail.html'
    context_object_name = 'envio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = self.object.productos.all()

        # Calculando el total de bultos (cantidad de productos)
        total_bultos = productos.count()

        # Calculando la suma del peso y volumen de todos los productos
        total_peso = sum(producto.peso for producto in productos)
        total_volumen = sum(producto.volumen for producto in productos)

        # Añadiendo estos valores al contexto
        context['productos'] = productos
        context['total_bultos'] = total_bultos
        context['total_peso'] = total_peso
        context['total_volumen'] = total_volumen
        return context
    
class EnvioCreateView(CreateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envios:envios_list')
    
class EnvioUpdateView(UpdateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envios/envio_form.html'
    success_url = reverse_lazy('envios:envios_list')
    
class EnvioDeleteView(DeleteView):
    model = Envio 
    success_url = reverse_lazy('envios:envios_list')