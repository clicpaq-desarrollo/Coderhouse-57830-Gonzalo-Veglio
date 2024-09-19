from django import forms
from miscelaneas.models import Localidad
from .models import Envio

class EnvioForm(forms.ModelForm):
    class Meta:
        model = Envio
        fields = [
            'cliente', 'destinatario_nombre', 'destinatario_direccion', 
            'destinatario_telefono', 'destinatario_email', 
            'destinatario_localidad'
        ]
        
    def __init__(self, *args, **kwargs):
        super(EnvioForm, self).__init__(*args, **kwargs)
        self.fields['destinatario_localidad'].queryset = Localidad.objects.all()  # Cargar todas las localidades

        self.fields['cliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['destinatario_nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['destinatario_direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['destinatario_telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['destinatario_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['destinatario_localidad'].widget.attrs.update({'class': 'form-control'})
