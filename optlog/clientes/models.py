from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)  
    direccion = models.CharField(max_length=255)  
    telefono = models.CharField(max_length=20)  
    email = models.EmailField(null=True, blank=True) 
    localidad = models.ForeignKey('miscelaneas.Localidad', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
         