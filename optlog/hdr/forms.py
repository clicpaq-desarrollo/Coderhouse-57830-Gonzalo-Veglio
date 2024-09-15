from django import forms
from .models import HojaDeRuta

class HdrForm(forms.ModelForm):
    class Meta:
        model = HojaDeRuta
        fields = '__all__' 
