from django.contrib import admin 

from . import models
#admin.site.register(Chofer)
 
@admin.register(models.Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ('envio', 'estado', 'ubicacion', 'fecha_actualizacion',) 
 


