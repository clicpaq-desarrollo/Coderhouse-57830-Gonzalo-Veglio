from django import forms
from .models import Tracking

class EnvioSearchForm(forms.Form):
    guia = forms.CharField(label='Número de guía', max_length=100)
    
    class Meta:
        fields = ['guia']
        widgets = {
            'guia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de guia'}),
        }

class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = ['estado', 'detalle']  
        widgets = {
            'estado': forms.Select(choices=Tracking.ESTADOS_ENVIO, attrs={'class': 'form-control'}),
            'detalle': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Detalle opcional'}),
        }
 