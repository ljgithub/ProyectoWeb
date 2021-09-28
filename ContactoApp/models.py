from django.db import models

# Create your models here.


class Contacto (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre