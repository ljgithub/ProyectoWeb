from BlogApp.views import blog, categoria
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', blog, name="Blog"),
    path('/categoria/<int:categoria_id>/', categoria, name="Categoria"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)