from django.contrib import admin 

from . import models
#admin.site.register(Chofer)
 
@admin.register(models.Chofer)
class ChoferAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono',)
    search_fields = ('nombre', )
    ordering = ('nombre',) 