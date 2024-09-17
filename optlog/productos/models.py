from django.db import models
from clientes.models import Cliente

class Producto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='productos')   
    nombre = models.CharField(max_length=255)  
    descripcion = models.TextField(blank=True, null=True)  
    peso = models.DecimalField(max_digits=6, decimal_places=2)  
    volumen = models.DecimalField(max_digits=6, decimal_places=2)  
    bultos = models.PositiveIntegerField(default=1)  
    fecha_ingreso = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
