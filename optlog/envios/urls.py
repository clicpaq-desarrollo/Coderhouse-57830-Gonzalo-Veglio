from django.urls import path
from .views import EnvioListView, EnvioCreateView, EnvioUpdateView, EnvioDeleteView, EnvioDetailView, EnvioBuscarDetailView, productos_por_cliente

from . import views
app_name = 'envios'

urlpatterns = [
    path('', EnvioListView.as_view(), name='envios_list'),
    path('create/', EnvioCreateView.as_view(), name='envio_create'),
    path('<int:pk>/edit/', EnvioUpdateView.as_view(), name='envio_edit'),
    path('<int:pk>/delete/', EnvioDeleteView.as_view(), name='envio_delete'),
    path('<int:pk>/', EnvioDetailView.as_view(), name='envio_detail'),
    path('detalle_envio/<int:pk>/', EnvioBuscarDetailView.as_view(), name='detalle_envio'),
    
    path('productos/', productos_por_cliente, name='productos_por_cliente'),
    path('productos_cliente/<int:cliente_id>/', views.productos_cliente, name='productos_cliente'),
]   
