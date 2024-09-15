from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from productos.models import Producto
import uuid

class Envio(models.Model):
    # Identificador único para la seguridad
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID generado automáticamente
    id_numero = models.PositiveIntegerField(unique=True, null=True, blank=True)  # ID numérico opcional y único
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='envios')  # Relación con el cliente
    productos = models.ManyToManyField(Producto)  # Productos asociados al envío
    destinatario_nombre = models.CharField(max_length=255)  # Nombre del destinatario
    destinatario_direccion = models.CharField(max_length=255)  # Dirección del destinatario
    destinatario_telefono = models.CharField(max_length=20)  # Teléfono del destinatario
    destinatario_email = models.EmailField()  # Correo electrónico del destinatario
    fecha_envio = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó el envío
    fecha_entrega = models.DateTimeField(null=True, blank=True)  # Fecha de entrega, puede estar vacía
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_transito', 'En tránsito'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ])  # Estado del envío
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Usuario que registró el envío

    def save(self, *args, **kwargs):
        # Asigna el id_numero solo si es None
        if self.id_numero is None:
            last_envio = Envio.objects.all().order_by('id_numero').last()
            self.id_numero = (last_envio.id_numero + 1) if last_envio else 100
        super(Envio, self).save(*args, **kwargs)

    def __str__(self):
        return f"Envío {self.id_numero} - {self.destinatario_nombre} - {self.estado}"

    class Meta:
        verbose_name = 'Envío'
        verbose_name_plural = 'Envios'