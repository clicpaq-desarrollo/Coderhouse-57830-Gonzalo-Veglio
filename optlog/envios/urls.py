from django.urls import path
from .views import EnvioListView, EnvioCreateView, EnvioUpdateView, EnvioDeleteView

app_name = 'envios'

urlpatterns = [
    path('admin-panel/envios/', EnvioListView.as_view(), name='envios_list'),
    path('admin-panel/envios/create/', EnvioCreateView.as_view(), name='envio_create'),
    path('admin-panel/envios/<int:pk>/edit/', EnvioUpdateView.as_view(), name='envio_edit'),
    path('admin-panel/envios/<int:pk>/delete/', EnvioDeleteView.as_view(), name='envio_delete'),
]