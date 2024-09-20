from django import forms
from .models import Cliente
from miscelaneas.models import Localidad  

class ClienteForm(forms.ModelForm):
    localidad = forms.ModelChoiceField(
        queryset=Localidad.objects.all(),  
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion', 'localidad']  
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
        }
