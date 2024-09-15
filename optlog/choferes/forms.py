from django import forms
from .models import Chofer

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = '__all__'
        widgets = {
             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
             'apellido': forms.TextInput(attrs={'class': 'form-control'}),
             'telefono': forms.TextInput(attrs={'class': 'form-control'}),
              
 
        }
