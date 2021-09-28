from django.contrib import admin

# Register your models here.
from TiendaApp.models import CategoriaP, Producto


class CategoriaP_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class Producto_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(CategoriaP ,CategoriaP_admin)
admin.site.register(Producto ,Producto_admin)