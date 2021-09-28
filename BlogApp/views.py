from django.shortcuts import render

# Create your views here.
from BlogApp.models import Categoria
from BlogApp.models import Post


def blog(request):
    lista_post  = Post.objects.all()
    return render(request, "blogs/blog.html", {"lista_post": lista_post})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    
    lista_post  = Post.objects.filter(categorias=categoria)

    return render(request, "blogs/categorias.html", {"lista_post": lista_post})