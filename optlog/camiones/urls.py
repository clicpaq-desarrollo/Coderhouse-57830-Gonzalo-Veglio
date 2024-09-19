from django.urls import path
from .views import CamionListView, CamionCreateView, CamionUpdateView, CamionDeleteView

app_name = 'camiones'

urlpatterns = [
    path('', CamionListView.as_view(), name='camiones_list'),
    path('create/', CamionCreateView.as_view(), name='camion_create'),
    path('<int:pk>/edit/', CamionUpdateView.as_view(), name='camion_edit'),
    path('<int:pk>/delete/', CamionDeleteView.as_view(), name='camion_delete'),
]