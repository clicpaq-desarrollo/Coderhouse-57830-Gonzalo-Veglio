from django.urls import path

from . import views

app_name = 'miscelaneas'


urlpatterns = [
    path('', views.index, name='index'), 
]