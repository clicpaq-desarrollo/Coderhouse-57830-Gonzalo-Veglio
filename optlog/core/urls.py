from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
