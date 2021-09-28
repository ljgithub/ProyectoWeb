def totalImportCart(request):
    priceProduct = 0.00
    #if request.user.is_authenticated:
    if 'cart' in request.session:
        for key, value in request.session["cart"].items():
            priceProduct = priceProduct + (float (value["precio_producto"]))
            priceProduct = round(priceProduct, 2)
    return {"importe_total_cart" : priceProduct}