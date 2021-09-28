from django.shortcuts import render, redirect
from urllib3.connection import log

from ShoppingCart.CaptureOrderFile import CaptureOrder
from ShoppingCart.GetOrderFile import GetOrder
from ShoppingCart.context_processor import totalImportCart
from ShoppingCart.ShoppingCart import ShoppingCart
from TiendaApp.models import Producto
from django.http import JsonResponse

import sys, json

def addProductView(request, idProduct):
    #1. Creamos el objeto ShoppingCart donde manejamos todo lo referente a la sesion
    cart = ShoppingCart(request)
    #2. Obtener el producto
    product = Producto.objects.get(id=idProduct)
    #3. Agregar a la sesion osea al carro
    cart.loadDataCart(product)

    return redirect("cartURL:pagar")

def deleteProductView(request, idProduct):
    #1. Creamos el objeto ShoppingCart donde manejamos todo lo referente a la sesion
    cart = ShoppingCart(request)
    #2. Obtener el producto
    product = Producto.objects.get(id=idProduct)
    #3. Agregar a la sesion osea al carro
    cart.deleteProduct(product)
    return redirect("cartURL:pagar")

def substractProductView(request, idProduct):
    #1. Creamos el objeto ShoppingCart donde manejamos todo lo referente a la sesion
    cart = ShoppingCart(request)
    #2. Obtener el producto
    product = Producto.objects.get(id=idProduct)
    #3. Agregar a la sesion osea al carro
    cart.substractProduct(product)

    return redirect("cartURL:pagar")

def cleanCartView(request):
    cart = ShoppingCart(request)
    cart.clearCartSession()
    return redirect("Tienda")

def cartView(request):
    ppclient_id = "AajqarWQaB3MyISiGqJLnlGr8o0JQaCUa7_SYfL1qOLGw4wI9CWuJZUgeKK_JdJgWmmY9pDZdkL7sAoW"
    print("Estoy en cartView")
    return render(request, "pago.html", {"ppclient": ppclient_id})

def pago(request):
    print("Entraste a la funcion Pago")
    pagoTotal = totalImportCart(request)
    pagoTotal = pagoTotal["importe_total_cart"]
    print("Total desde context", pagoTotal)
    dataBody = json.loads(request.body)
    orden_id = dataBody['orderID']
    print("Id Orden: ", orden_id)

    orden = GetOrder().get_order(orden_id)
    print("La orden es: ", orden)
    orden_total = float(orden.result.purchase_units[0].amount.value)
    print ("El valor total es : " + str(orden_total))

    if orden_total == pagoTotal:
        transaccion = CaptureOrder().capture_order(orden_id)
        pedido = {
            "id_transaccion" : transaccion.result.id,
            "nombre_cliente" : transaccion.result.payer.name.given_name,
            "mensaje" : " :D "
        }

        # Una vez completada la fase de pago de la transaccion se requiere
        # 1. Igualar a cero el importe total de la variable usada en el context_processor
        # 2. Vaciar la sesion del usuario actual

        # 2. Con las siguientes dos lineas vaciamos la sesion por ende el importe total del context
        cart = ShoppingCart(request)
        cart.clearCartSession()

        return JsonResponse(pedido)
    else:
        pedido = {
            "mensaje" : "Error :c"
        }
        return JsonResponse(pedido)

def payment_complete(request):
    return render(request, "payment_complete.html")