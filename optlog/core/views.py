from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 
 
from django.http import JsonResponse
from envios.models import Envio

from .forms import CustomUserCreationForm, UserProfileForm

 
from django.shortcuts import render, redirect
from envios.models import Envio

def buscar_envio(request):
    guia = request.GET.get('guia')  
    if guia:
        try:
            envio = Envio.objects.get(guia=guia)
        
            return redirect('envios:detalle_envio', pk=envio.pk)
        except Envio.DoesNotExist:
        
            return render(request, 'core/index.html', {
                'error': 'El envío con esa guía no existe.'
            })

    return render(request, 'core/index.html')



def index(request):
     return render(request, 'core/index.html')



def admin_panel(request):
    return render(request, 'core/admin_panel.html')

 

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('core:index')

    def get_object(self):
         
        return self.request.user
 