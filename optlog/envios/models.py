from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from productos.models import Producto

class Envio(models.Model):
    guia = models.PositiveIntegerField(unique=True, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='envios')
    productos = models.ManyToManyField(Producto)
    destinatario_nombre = models.CharField(max_length=255)
    destinatario_direccion = models.CharField(max_length=255)
    destinatario_telefono = models.CharField(max_length=20)
    destinatario_email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    anula = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.guia is None:
            last_envio = Envio.objects.all().order_by('guia').last()
            self.guia = (last_envio.guia + 1) if last_envio else 100

        if not self.pk and self.usuario is None:
            self.usuario = kwargs.pop('usuario', None)

        super(Envio, self).save(*args, **kwargs)

        # Crear el registro en Tracking después de guardar el Envio
        from tracking.models import Tracking  # Importar localmente para evitar circular imports
        if not Tracking.objects.filter(envio=self).exists():
            Tracking.objects.create(
                envio=self,
                estado='en_proceso_despacho',
                usuario=self.usuario
            )

    def __str__(self):
        return f"Guía {self.guia} - {self.destinatario_nombre}"

    class Meta:
        verbose_name = 'Envío'
        verbose_name_plural = 'Envios'
