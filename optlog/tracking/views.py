from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Tracking
from envios.models import Envio
from .forms import TrackingForm

class AddTrackingView(View):
    def get(self, request):
        form = TrackingForm()
        return render(request, 'tracking/tracking_add.html', {'form': form})
    
    def post(self, request):
        form = TrackingForm(request.POST)
        if form.is_valid():
            guia = form.cleaned_data['guia']
            envio = get_object_or_404(Envio, guia=guia)
            tracking = form.save(commit=False)
            tracking.envio = envio
            tracking.save()
            return redirect('tracking:tracking_list')
        return render(request, 'tracking/add_tracking.html', {'form': form})
