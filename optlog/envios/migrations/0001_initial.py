# Generated by Django 5.1.1 on 2024-09-16 20:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('miscelaneas', '0001_initial'),
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia', models.PositiveIntegerField(editable=False, unique=True)),
                ('destinatario_nombre', models.CharField(max_length=255)),
                ('destinatario_direccion', models.CharField(max_length=255)),
                ('destinatario_telefono', models.CharField(max_length=20)),
                ('destinatario_email', models.EmailField(max_length=254)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('anula', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envios', to='clientes.cliente')),
                ('destinatario_localidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miscelaneas.localidad')),
                ('usuario', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Envío',
                'verbose_name_plural': 'Envios',
            },
        ),
        migrations.CreateModel(
            name='ProductoEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('envio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productoenvios', to='envios.envio')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='envio',
            name='productos',
            field=models.ManyToManyField(through='envios.ProductoEnvio', to='productos.producto'),
        ),
    ]
