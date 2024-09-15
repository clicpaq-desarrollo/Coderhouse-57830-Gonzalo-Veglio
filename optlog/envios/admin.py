from django.contrib import admin
from . import models

@admin.register(models.Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = ('id_numero','fecha_envio','cliente','destinatario_nombre','estado')
    search_fields = ('cliente','destinatario_nombre', )
    ordering = ('id_numero',) 
 