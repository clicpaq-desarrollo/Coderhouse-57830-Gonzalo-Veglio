from django.db import models

class Pedido(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    destinatario_nombre = models.CharField(max_length=50)
    destinatario_apellido = models.CharField(max_length=50)
    destinatario_telefono = models.CharField(max_length=20)
    destinatario_localidad = models.ForeignKey('miscelaneas.Localidad', on_delete=models.CASCADE)
    articulo = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('entregado', 'Entregado')])

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - {self.articulo.descripcion}"
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
