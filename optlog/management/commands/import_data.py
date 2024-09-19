from django.core.management.base import BaseCommand
from productos.models import Producto
from clientes.models import Cliente

class Command(BaseCommand):
    help = 'Carga datos de productos desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('archivo', type=str)

    def handle(self, *args, **kwargs):
        archivo = kwargs['archivo']
        with open(archivo, 'r') as file:
            for line in file:
               
               
                fields = line.strip().split(',')
                cliente_id, nombre, descripcion, peso, volumen, bultos = fields
                
               
                cliente = Cliente.objects.get(id=cliente_id)
                
               
                Producto.objects.create(
                    cliente=cliente,
                    nombre=nombre,
                    descripcion=descripcion,
                    peso=peso,
                    volumen=volumen,
                    bultos=bultos
                )
                
        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente.'))
