from django.urls import path
from .views import HdrListView, HdrCreateView, HdrUpdateView, HdrDeleteView

app_name = 'hdr'

urlpatterns = [
    path('admin-panel/hdr/', HdrListView.as_view(), name='hdrs_list'),
    path('admin-panel/hdr/create/', HdrCreateView.as_view(), name='hdr_create'),
    path('admin-panel/hdr/<int:pk>/edit/', HdrUpdateView.as_view(), name='hdr_edit'),
    path('admin-panel/hdr/<int:pk>/delete/', HdrDeleteView.as_view(), name='hdr_delete'),
]