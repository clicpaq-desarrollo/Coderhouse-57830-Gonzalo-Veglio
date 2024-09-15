from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  
        widgets = {
             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'telefono': forms.TextInput(attrs={'class': 'form-control'}), 
            'direccion': forms.TextInput(attrs={'class': 'form-control'}), 

        }
