from ProyectoWebApp.views import home, contacto, blog, tienda
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [        
    path('', home, name= "Home"),
]

#Esta linea sirve para que el navegador pueda abrir la imagen
# desde el administrador del sitio para cada
# seccion de las aplicaciones creadas

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)