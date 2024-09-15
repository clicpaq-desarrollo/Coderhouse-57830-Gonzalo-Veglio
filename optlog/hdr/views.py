from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import HojaDeRuta
from .forms import HdrForm

class HdrListView(ListView):
    model = HojaDeRuta
    template_name = 'hdr/hdr_list.html'
    context_object_name = 'hdres'

class HdrDetailView(DetailView):
    model = HojaDeRuta
    template_name = 'hdr/hdr_detail.html'
    context_object_name = 'hdr'
    
class HdrCreateView(CreateView):
    model = HojaDeRuta
    form_class = HdrForm
    template_name = 'hdr/hdr_form.html'
    success_url = reverse_lazy('hdres:hdr_list')
    
class HdrUpdateView(UpdateView):
    model = HojaDeRuta
    form_class = HdrForm
    template_name = 'hdr/hdr_form.html'
    success_url = reverse_lazy('hdres:hdr_list')
    
class HdrDeleteView(DeleteView):
    model = HojaDeRuta
    template_name = 'hdr/hdr_delete.html'
    success_url = reverse_lazy('hdres:hdr_list')