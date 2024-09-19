from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from .forms import EnvioSearchForm, TrackingForm
from .models import Tracking
from envios.models import Envio

class TrazabilidadUpdateView(FormView):
    template_name = 'tracking/tracking_add.html'
    form_class = EnvioSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracking_form'] = TrackingForm()
        return context

    def post(self, request, *args, **kwargs):
        search_form = self.get_form()
        if search_form.is_valid():
            guia = search_form.cleaned_data['guia']
            envio = get_object_or_404(Envio, guia=guia)
            tracking_form = TrackingForm(request.POST)
            if tracking_form.is_valid():
                tracking = tracking_form.save(commit=False)
                tracking.envio = envio
                tracking.usuario = request.user
                tracking.save()
                return redirect('envios:envios_list')  
            return self.render_to_response(self.get_context_data(envio=envio, tracking_form=tracking_form))
        return self.form_invalid(search_form)
