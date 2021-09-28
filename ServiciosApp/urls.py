from ServiciosApp.views import servicios
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', servicios, name="Servicios"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)