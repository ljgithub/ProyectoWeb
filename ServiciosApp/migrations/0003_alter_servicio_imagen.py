# Generated by Django 3.2.4 on 2021-06-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0002_alter_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='media/servicios_media'),
        ),
    ]
