from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

app_name = 'productos'

urlpatterns = [
    path('admin-panel/productos/', ProductoListView.as_view(), name='productos_list'),
    path('admin-panel/productos/create/', ProductoCreateView.as_view(), name='producto_create'),
    path('admin-panel/productos/<int:pk>/edit/', ProductoUpdateView.as_view(), name='producto_edit'),
    path('admin-panel/productos/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto_delete'),
]