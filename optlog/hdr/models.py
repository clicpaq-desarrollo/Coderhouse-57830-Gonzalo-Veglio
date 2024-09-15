from django.db import models
from camiones.models import Camion
from choferes.models import Chofer
from envios.models import Envio

class HojaDeRuta(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)  # Camión asignado a la ruta
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)  # Chofer asignado a la ruta
    envios = models.ManyToManyField(Envio)  # Envíos incluidos en la hoja de ruta
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó la hoja de ruta
    fecha_salida = models.DateTimeField(null=True, blank=True)  # Fecha de salida de la ruta
    fecha_llegada = models.DateTimeField(null=True, blank=True)  # Fecha de llegada de la ruta

    def __str__(self):
        return f"Hoja de Ruta {self.id} - Camión {self.camion.patente}"
    
    class Meta:
        verbose_name = 'Hoja de Ruta'
        verbose_name_plural = 'Hojas de Ruta'
        
         