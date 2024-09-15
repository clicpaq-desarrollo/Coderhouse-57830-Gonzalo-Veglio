from django.db import models
from envios.models import Envio

class Tracking(models.Model):
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE, related_name='tracking')  # Relación con el envío
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_transito', 'En tránsito'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ])  # Estado del envío en este punto del seguimiento
    ubicacion = models.CharField(max_length=255, null=True, blank=True)  # Ubicación opcional del envío
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)  # Fecha de actualización del estado

    def __str__(self):
        return f"Tracking {self.envio.id} - {self.estado}"
    
    class Meta:
        verbose_name = 'Tracking'
        verbose_name_plural = 'Trackings'