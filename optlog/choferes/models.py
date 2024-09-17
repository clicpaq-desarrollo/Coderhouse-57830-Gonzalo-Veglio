from django.db import models

class Chofer(models.Model):
    nombre = models.CharField(max_length=255) 
    apellido = models.CharField(max_length=255) 
    telefono = models.CharField(max_length=20) 
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'