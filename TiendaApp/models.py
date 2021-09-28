from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CategoriaP(models.Model):
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoriaP"
        verbose_name_plural = "categoriasP"

    def __str__(self):
        return  self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, max_digits=9)
    imagen = models.ImageField(upload_to= "media/productos_media", null= True, blank=True)

    categorias = models.ForeignKey(CategoriaP, on_delete=models.CASCADE)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return  self.nombre