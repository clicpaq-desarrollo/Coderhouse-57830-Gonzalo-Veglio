from django import forms
from .models import Envio, ProductoEnvio
from productos.models import Producto
from miscelaneas.models import Localidad

class EnvioForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Envio
        fields = [
            'cliente',
            'destinatario_nombre',
            'destinatario_direccion',
            'destinatario_telefono',
            'destinatario_email',
            'destinatario_localidad',
            'productos'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'destinatario_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario_direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario_telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'destinatario_localidad': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EnvioForm, self).__init__(*args, **kwargs)
        if 'cliente' in self.data:
            self.fields['productos'].queryset = Producto.objects.filter(cliente=self.data['cliente'])
