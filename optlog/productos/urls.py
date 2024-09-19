from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

app_name = 'productos'

urlpatterns = [
    path('', ProductoListView.as_view(), name='productos_list'),
    path('create/', ProductoCreateView.as_view(), name='producto_create'),
    path('<int:pk>/edit/', ProductoUpdateView.as_view(), name='producto_edit'),
    path('<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto_delete'),
]