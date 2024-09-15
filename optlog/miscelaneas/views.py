from django.shortcuts import render

from .models import Localidad

def index(request):
    return render(request, 'miscelaneas/index.html')