from django.contrib import admin
from .models import Envio
from .forms import EnvioForm   

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    form = EnvioForm
    list_display = ('guia', 'cliente', 'destinatario_nombre', 'fecha_creacion')
    search_fields = ('guia', 'cliente__nombre', 'destinatario_nombre')
    ordering = ('-fecha_creacion',)
    exclude = ('anula',)  
