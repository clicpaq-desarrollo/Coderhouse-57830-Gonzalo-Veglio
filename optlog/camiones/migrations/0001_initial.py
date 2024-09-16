# Generated by Django 5.1.1 on 2024-09-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10)),
                ('capacidad_maxima', models.DecimalField(decimal_places=2, max_digits=6)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Camión',
                'verbose_name_plural': 'Camiones',
            },
        ),
    ]
