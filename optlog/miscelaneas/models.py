from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.localidad}, {self.provincia}"

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
