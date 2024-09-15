"""
URL configuration for optlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from camiones import urls
from choferes import urls
from clientes import urls
from core import views
from envios import urls
from hdr import urls
from miscelaneas import urls
from productos import urls
from tracking import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('camiones/', include('camiones.urls')),
    path('choferes/', include('choferes.urls')),
    path('clientes/', include('clientes.urls')),
    path('envios/', include('envios.urls')),
    path('hdr/', include('hdr.urls')),
    path('miscelaneas/', include('miscelaneas.urls')),
    path('productos/', include('productos.urls')),
    path('tracking/', include('tracking.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', include('core.urls')), 
 ]