from django.http import HttpResponse
from django.shortcuts import render
from ServiciosApp.models import Servicio

# Create your views here.
def home(request):
    return render(request, "home.html")
    
def tienda(request):
    return render(request, "tienda.html")

def blog(request):
    return render(request, "blog.html")

def contacto(request):
    return render(request, "contacto.html")        