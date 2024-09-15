from django.contrib import admin
from . import models

@admin.register(models.HojaDeRuta)
class HojaDeRutaAdmin(admin.ModelAdmin):
    list_display = ('fecha_creacion', 'get_camion', 'get_chofer', 'get_envios', 'fecha_salida')
    search_fields = ('camion__nombre', 'chofer__nombre')  # Ajusta los nombres de los campos según tu modelo
    ordering = ('camion', 'chofer')  # Considera usar los campos adecuados para ordenar

    def get_camion(self, obj):
        return obj.camion.nombre  # Ajusta según el campo del modelo Camion que deseas mostrar

    def get_chofer(self, obj):
        return obj.chofer.nombre  # Ajusta según el campo del modelo Chofer que deseas mostrar

    def get_envios(self, obj):
        return ", ".join([envio.descripcion for envio in obj.envios.all()])  # Ajusta según tu modelo Envio

    get_camion.short_description = 'Camion'
    get_chofer.short_description = 'Chofer'
    get_envios.short_description = 'Envios'
