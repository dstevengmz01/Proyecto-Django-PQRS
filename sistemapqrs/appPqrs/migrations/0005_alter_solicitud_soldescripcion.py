# Generated by Django 5.0.2 on 2025-06-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPqrs', '0004_usuario_usotipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='solDescripcion',
            field=models.TextField(blank=True),
        ),
    ]
