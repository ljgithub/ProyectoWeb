from ServiciosApp.models import Servicio 
from django.contrib import admin

# Register your models here.

class Servicio_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
admin.site.register(Servicio, Servicio_admin)