from django.urls import path
from .views import CamionListView, CamionCreateView, CamionUpdateView, CamionDeleteView

app_name = 'camiones'

urlpatterns = [
    path('admin-panel/camiones/', CamionListView.as_view(), name='camiones_list'),
    path('admin-panel/camiones/create/', CamionCreateView.as_view(), name='camion_create'),
    path('admin-panel/camiones/<int:pk>/edit/', CamionUpdateView.as_view(), name='camion_edit'),
    path('admin-panel/camiones/<int:pk>/delete/', CamionDeleteView.as_view(), name='camion_delete'),
]