from django.db import models

class Camion(models.Model):
    patente = models.CharField(max_length=10)  
    capacidad_maxima = models.DecimalField(max_digits=6, decimal_places=2)  
    marca = models.CharField(max_length=50)  
    modelo = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"
    
    class Meta:
        verbose_name = 'Camión'
        verbose_name_plural = 'Camiones'