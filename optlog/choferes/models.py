from django.db import models

class Chofer(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del chofer
    apellido = models.CharField(max_length=255)  # Apellidos del chofer 
    telefono = models.CharField(max_length=20)  # Teléfono del chofer
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'