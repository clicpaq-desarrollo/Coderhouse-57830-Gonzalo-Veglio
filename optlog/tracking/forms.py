from django import forms
from .models import Tracking

class TrackingForm(forms.ModelForm):
    guia = forms.IntegerField(label='Número de Guía')

    class Meta:
        model = Tracking
        fields = ['estado']
    
    def clean_guia(self):
        guia = self.cleaned_data.get('guia')
        if not Envio.objects.filter(guia=guia).exists():
            raise forms.ValidationError("El número de guía no existe.")
        return guia
