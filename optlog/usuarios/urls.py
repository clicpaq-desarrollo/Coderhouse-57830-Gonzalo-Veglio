
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('edit-profile/', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)