from django.db import models

 
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True , blank=False)
    
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'