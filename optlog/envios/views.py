from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Envio
from .forms import EnvioForm

class EnvioListView(ListView):
    model = Envio
    template_name = 'envio/envio_list.html'
    context_object_name = 'envio'

class EnvioDetailView(DetailView):
    model = Envio
    template_name = 'envio/envio_detail.html'
    context_object_name = 'envio'
    
class EnvioCreateView(CreateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envio/envio_form.html'
    success_url = reverse_lazy('envio:envio_list')
    
class EnvioUpdateView(UpdateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'envio/envio_form.html'
    success_url = reverse_lazy('envio:envio_list')
    
class EnvioDeleteView(DeleteView):
    model = Envio
    template_name = 'envio/envio_delete.html'
    success_url = reverse_lazy('envio:envio_list')