from paypalcheckoutsdk.orders import OrdersGetRequest
from ShoppingCart.PayPalClientFile import PayPalClient

class GetOrder(PayPalClient):
    #2. Habilitamos el servidor para recibir llamadas desde el cliente
    """Puedes usar esta funcion para recibir un detalle de la orden pasandole su id como argumento"""
    def get_order(self, order_id):
        """Metodo para obtener la orden"""
        print("La orden en la clase GetOrder es: ", order_id)
        request = OrdersGetRequest(order_id)
        print(request.body)
        #3. Llama a Paypal para obtener una transaccion
        response = self.client.execute(request)
        #4. Guarda la transaccion en su base de datos e implementa la logica respectiva.
        print ('Status Code: ', response.status_code)
        print ('Status: ', response.result.status)
        print ('Order ID: ', response.result.id)
        print ('Intent: ', response.result.intent)
        print ('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))

        print ('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                           response.result.purchase_units[0].amount.value) )



        """This driver function invokes the get_order function with
           order ID to retrieve sample order details. """
        #if __name__ == '__main__':
        #    GetOrder().get_order('REPLACE-WITH-VALID-ORDER-ID')

        return response