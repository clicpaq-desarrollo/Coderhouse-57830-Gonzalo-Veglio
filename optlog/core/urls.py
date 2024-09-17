from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomLoginForm
from . import views

app_name = 'core'
    
urlpatterns = [
    path('', views.index, name='index'),
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
