from django.db import models

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.localidad + ", " + self.provincia

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

 