from django.contrib import admin

from . import models 

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono', 'direccion',)
    search_fields = ('nombre', )
    ordering = ('nombre',) 
