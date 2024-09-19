from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from productos.models import Producto
from miscelaneas.models import Localidad, Provincia

class ProductoEnvio(models.Model):
    envio = models.ForeignKey('Envio', on_delete=models.CASCADE, related_name='productoenvios')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class Envio(models.Model):
    guia = models.PositiveIntegerField(unique=True, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='envios')
    productos = models.ManyToManyField(Producto, through='ProductoEnvio')
    destinatario_nombre = models.CharField(max_length=255)
    destinatario_direccion = models.CharField(max_length=255)
    destinatario_telefono = models.CharField(max_length=20)
    destinatario_email = models.EmailField(null=True, blank=True)
    destinatario_localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True)
        
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    anula = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    @property
    def peso_total(self):
        return sum(
            producto.peso * productoenvio.cantidad
            for productoenvio in self.productoenvios.all()
            for producto in [productoenvio.producto]
        )

    @property
    def volumen_total(self):
        return sum(
            producto.volumen * productoenvio.cantidad
            for productoenvio in self.productoenvios.all()
            for producto in [productoenvio.producto]
        )
    
    @property
    def cantidad_bultos(self):
        return sum(
            producto.bultos * productoenvio.cantidad
            for productoenvio in self.productoenvios.all()
            for producto in [productoenvio.producto]
        )

    def save(self, *args, **kwargs):
        if self.guia is None:
            last_envio = Envio.objects.all().order_by('guia').last()
            self.guia = (last_envio.guia + 1) if last_envio else 100

        if not self.pk and self.usuario is None:
            self.usuario = kwargs.pop('usuario', None)

        super(Envio, self).save(*args, **kwargs)

        from tracking.models import Tracking
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
