from django.urls import path

from ShoppingCart import views

#Poner app_name es como usar un namespace para anteponer primero la palabra de app_name y luego del nombre de la URLc
app_name = "cartURL"

urlpatterns = [
    path("agregar/<int:idProduct>/", views.addProductView, name="agregar"),
    path("eliminar/<int:idProduct>/", views.deleteProductView, name="eliminar"),
    path("restar/<int:idProduct>/", views.substractProductView, name="restar"),
    path("limpiar/", views.cleanCartView, name="limpiar"),

    path('', views.cartView, name="pagar"),
    path('checkout', views.pago, name="checkout"),
    path('payment_complete', views.payment_complete, name="pago_completo"),
]
