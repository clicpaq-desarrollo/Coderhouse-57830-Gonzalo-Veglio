from django.contrib import admin
from .models import Envio

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = ('guia', 'cliente', 'destinatario_nombre', 'fecha_creacion', 'anula')
    search_fields = ('cliente__nombre', 'destinatario_nombre', 'guia')
    ordering = ('guia', 'fecha_creacion')
    list_filter = ('anula', 'cliente')

    # Opcionalmente, puedes añadir campos de solo lectura como 'fecha_creacion'
    readonly_fields = ('fecha_creacion',)

    # Customiza el formulario de creación/edición si es necesario
    fields = ('cliente', 'productos', 'destinatario_nombre', 'destinatario_direccion', 'destinatario_telefono', 'destinatario_email', 'anula')
 