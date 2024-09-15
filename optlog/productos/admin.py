from django.contrib import admin 

from . import models
#admin.site.register(Chofer)
 
@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'nombre', 'descripcion', 'peso','volumen', 'fecha_ingreso')
    search_fields = ('nombre', 'descripcion', 'cliente', )
    ordering = ('nombre',) 
    
 