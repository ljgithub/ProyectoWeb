# Generated by Django 3.2.4 on 2021-08-21 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'categoriaP',
                'verbose_name_plural': 'categoriasP',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/productos_media')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('disponibilidad', models.BooleanField(default=True)),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TiendaApp.categoriap')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
