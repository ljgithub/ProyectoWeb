from django.shortcuts import render

# Create your views here.
from ServiciosApp.models import Servicio


def servicios(request):

    listaServicios  = Servicio.objects.all()

    return render(request, "servicios/servicios.html", {"listaServicios": listaServicios})