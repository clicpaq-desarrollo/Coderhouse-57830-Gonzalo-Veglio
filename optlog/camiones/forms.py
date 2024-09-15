from django import forms
from .models import Camion

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = '__all__' 
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_maxima': forms.NumberInput(attrs={'class': 'form-control'}), 
            'marca': forms.TextInput(attrs={'class': 'form-control'}), 
            'modelo': forms.TextInput(attrs={'class': 'form-control'}), 

        }



