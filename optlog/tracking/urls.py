from django.urls import path
from .views import TrazabilidadUpdateView

app_name = 'tracking'

urlpatterns = [
    path('actualizar-trazabilidad/', TrazabilidadUpdateView.as_view(), name='trazabilidad_update'),
]
