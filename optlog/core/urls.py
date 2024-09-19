from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomLoginForm
from . import views
from .views import buscar_envio

app_name = 'core'
    
urlpatterns = [
    path('', views.index, name='index'),  # Vista principal de index
    path('buscar/', views.buscar_envio, name='buscar_envio'),  # Ruta para buscar envíos
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('login', LoginView.as_view(
        template_name='core/login.html', 
        authentication_form=CustomLoginForm), 
        name='login'
    ),
    path('logout', LogoutView.as_view(next_page='core:index'), name='logout'),  
    path('register', views.Register.as_view(), name='register'),
    path('profile', views.Profile.as_view(), name='profile'),
]