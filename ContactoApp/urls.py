from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ContactoApp.views import contacto

urlpatterns = [
    path('', contacto, name="Contacto"),
    #path('/contacto/<slug:ref>/', contacto, name="Contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)