from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Chofer
from .forms import ChoferForm

class ChoferListView(ListView):
    model = Chofer
    template_name = 'choferes/choferes_list.html'
    context_object_name = 'choferes'
    
class ChoferDetailView(DetailView):
    model = Chofer
    template_name = 'choferes/chofer_detail.html'
    context_object_name = 'chofer'

class ChoferCreateView(CreateView):
    model = Chofer
    form_class = ChoferForm
    template_name = 'choferes/chofer_form.html'
    success_url = reverse_lazy('choferes:choferes_list')

class ChoferUpdateView(UpdateView):
    model = Chofer
    form_class = ChoferForm
    template_name = 'choferes/chofer_form.html'
    success_url = reverse_lazy('choferes:choferes_list')

class ChoferDeleteView(DeleteView):
    model = Chofer 
    success_url = reverse_lazy('choferes:choferes_list')
