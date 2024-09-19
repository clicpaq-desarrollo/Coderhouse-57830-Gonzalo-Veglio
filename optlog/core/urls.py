from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from django.views.generic import RedirectView
from .forms import CustomLoginForm
from . import views
from .views import buscar_envio

app_name = 'core'
    
urlpatterns = [
    path('index/', views.index, name='index'),  
     path('', RedirectView.as_view(url='/graficos/mostrar/', permanent=False), name='home'),
   
    path('buscar/', views.buscar_envio, name='buscar_envio'),  
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