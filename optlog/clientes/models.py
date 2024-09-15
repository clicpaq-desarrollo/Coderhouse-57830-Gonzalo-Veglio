from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del cliente
    direccion = models.CharField(max_length=255)  # Dirección del cliente
    telefono = models.CharField(max_length=20)  # Teléfono del cliente
    email = models.EmailField(null=True, blank=True) 
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
         