# Generated by Django 4.2 on 2023-04-22 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': [('Administrador', 'Utilização das funções gerais do sistema')]},
        ),
    ]
