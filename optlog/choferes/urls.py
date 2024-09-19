from django.urls import path
from .views import ChoferListView, ChoferCreateView, ChoferUpdateView, ChoferDeleteView

app_name = 'choferes'

urlpatterns = [
    path('', ChoferListView.as_view(), name='choferes_list'),
    path('crear/', ChoferCreateView.as_view(), name='chofer_create'),
    path('editar/<int:pk>/', ChoferUpdateView.as_view(), name='chofer_edit'),
    path('borrar/<int:pk>/', ChoferDeleteView.as_view(), name='chofer_delete'),
]
 