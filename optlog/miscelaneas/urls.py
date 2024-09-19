# miscelaneas/urls.py

from django.urls import path
from . import views

app_name = 'miscelaneas'

urlpatterns = [
    # Elimina esta línea, ya que no es necesaria
    # path('localidad/<int:provincia_id>/', views.localidades_por_provincia, name='localidades_por_provincia'),
]
