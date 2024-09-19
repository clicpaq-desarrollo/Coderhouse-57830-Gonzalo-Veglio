from django.urls import path
from . import views
from .views import datos_kilos_por_cliente

app_name = 'graficos'

urlpatterns = [
    path('mostrar/', views.mostrar_graficos, name='mostrar_graficos'),
    path('grafico-envios-cliente/', views.datos_envios_por_cliente, name='datos_envios_por_cliente'),
    path('datos-kilos-por-cliente/', datos_kilos_por_cliente, name='datos_kilos_por_cliente'),
   
]
