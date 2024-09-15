from django.contrib import admin 

from . import models
#admin.site.register(Chofer)
 
@admin.register(models.Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'patente', 'capacidad_maxima',)
    search_fields = ('marca', 'modelo', 'patente', )
    ordering = ('marca', 'modelo',) 
    
