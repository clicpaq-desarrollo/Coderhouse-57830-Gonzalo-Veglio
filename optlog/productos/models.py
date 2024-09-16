from django.db import models
from clientes.models import Cliente

class Producto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='productos')  # Relación con el cliente
    nombre = models.CharField(max_length=255)  # Nombre del producto
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional del producto
    peso = models.DecimalField(max_digits=6, decimal_places=2)  # Peso del producto en unidades apropiadas
    volumen = models.DecimalField(max_digits=6, decimal_places=2)  # Volumen del producto en unidades apropiadas
    bultos = models.PositiveIntegerField(default=1)  # Agregado para representar los bultos
    fecha_ingreso = models.DateTimeField(auto_now_add=True)  # Fecha en que se ingresó el producto
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
