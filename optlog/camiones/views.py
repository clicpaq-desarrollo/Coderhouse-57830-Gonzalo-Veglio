from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Camion
from .forms import CamionForm

class CamionListView(LoginRequiredMixin, ListView):
    model = Camion
    template_name = 'camiones/camiones_list.html'
    context_object_name = 'camiones'

class CamionDetailView(LoginRequiredMixin, DetailView):
    model = Camion
    template_name = 'camiones/camion_detail.html'
    context_object_name = 'camion'
    
class CamionCreateView(LoginRequiredMixin, CreateView):
    model = Camion
    form_class = CamionForm
    template_name = 'camiones/camion_form.html'
    success_url = reverse_lazy('camiones:camiones_list')
    
class CamionUpdateView(LoginRequiredMixin, UpdateView):
    model = Camion
    form_class = CamionForm
    template_name = 'camiones/camion_form.html'
    success_url = reverse_lazy('camiones:camiones_list')
    
class CamionDeleteView(LoginRequiredMixin, DeleteView):
    model = Camion 
    success_url = reverse_lazy('camiones:camiones_list')