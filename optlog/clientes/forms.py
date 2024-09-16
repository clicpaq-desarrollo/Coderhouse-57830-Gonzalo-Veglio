from django import forms
from .models import Cliente
from miscelaneas.models import Localidad

class ClienteForm(forms.ModelForm):
    # Aquí configuramos el campo localidad como un ModelChoiceField
    localidad = forms.ModelChoiceField(queryset=Localidad.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = '__all__'  
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'telefono': forms.TextInput(attrs={'class': 'form-control'}), 
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
