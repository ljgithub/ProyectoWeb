import cart as cart

from TiendaApp.models import Producto


class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get("cart")

        if not self.cart:
            self.cart = self.session["cart"] = {}


    def loadDataCart(self, producto):
        if str(producto.id) not in self.cart.keys():

            self.cart[producto.id] = {"producto_id" : producto.id,
                                 "nombre_producto" : producto.nombre,
                                 "descrip_producto" : producto.descripcion,
                                 "precio_producto" : str(producto.precio),
                                 "imagen_producto" : producto.imagen.url,
                                 "cantidad_producto" : 1,
                                 }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad_producto"] = value["cantidad_producto"] + 1
                    if value["cantidad_producto"] > 1 :
                        value["precio_producto"] = float(producto.precio) * float(value["cantidad_producto"])
                    break

        self.saveCart()

    def saveCart(self):
        self.session["cart"] = self.cart
        self.session.modified = True


    def substractProduct(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value["cantidad_producto"] = value["cantidad_producto"] - 1
                if value["cantidad_producto"] >= 1 :
                    value["precio_producto"] = float(producto.precio) * float(value["cantidad_producto"])

                if value["cantidad_producto"] == 0:
                    self.deleteProduct(producto)
                break
        self.saveCart()

    def deleteProduct(self, producto):
        idProducto = str(producto.id)
        if idProducto in self.cart:
            del self.cart[idProducto]
            self.saveCart()

    def clearCartSession(self):
        self.cart = {}
        self.saveCart()