from django.contrib import admin
from .models import Localidad, Provincia

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('localidad', 'provincia')
    search_fields = ('localidad', 'provincia__nombre')   
    ordering = ('localidad',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
