from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

app_name = 'clientes'

urlpatterns = [
    path('admin-panel/clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('admin-panel/clientes/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('admin-panel/clientes/<int:pk>/edit/', ClienteUpdateView.as_view(), name='cliente_edit'),
    path('admin-panel/clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
