from django.contrib import admin
from ContactoApp.models import Contacto

# Register your models here.

class Contacto_admin(admin.ModelAdmin):
    readonly_fields = ( "created", "updated")

admin.site.register(Contacto,  Contacto_admin)