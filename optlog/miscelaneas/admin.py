from django.contrib import admin


from . import models

@admin.register(models.Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('localidad', 'provincia')
    search_fields = ('localidad', 'provincia')
    ordering = ('localidad',)