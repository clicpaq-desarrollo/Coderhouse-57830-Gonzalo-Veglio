from django.db import models
from django.contrib.auth.models import User

class Tracking(models.Model):
    envio = models.ForeignKey('envios.Envio', on_delete=models.CASCADE, related_name='tracking')  # Lazy reference
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_transito', 'En tránsito'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ])
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Tracking {self.envio.guia} - {self.estado}"
    
    class Meta:
        verbose_name = 'Tracking'
        verbose_name_plural = 'Trackings'
