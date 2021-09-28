# Create your views here.

from django.shortcuts import render

from TiendaApp.models import Producto


def tienda(request):
    lista_productos = Producto.objects.all()
    return render(request , 'tienda.html' , {'lista_productos': lista_productos})
