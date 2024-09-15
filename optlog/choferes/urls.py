from django.urls import path
from .views import ChoferListView, ChoferCreateView, ChoferUpdateView, ChoferDeleteView

app_name = 'choferes'

urlpatterns = [
    path('admin-panel/choferes/', ChoferListView.as_view(), name='choferes_list'),
    path('admin-panel/choferes/crear/', ChoferCreateView.as_view(), name='chofer_create'),
    path('admin-panel/choferes/editar/<int:pk>/', ChoferUpdateView.as_view(), name='chofer_edit'),
    path('admin-panel/choferes/borrar/<int:pk>/', ChoferDeleteView.as_view(), name='chofer_delete'),
]
 