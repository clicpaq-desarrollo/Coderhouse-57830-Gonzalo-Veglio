# Generated by Django 5.1.1 on 2024-09-14 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelaneas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='cliente',
        ),
    ]
