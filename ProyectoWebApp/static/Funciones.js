function dataSendedSucess() {
    //alert("Estoy en la funcion");
    swal("Excelente!", "Tu información ha sido enviada correctamente!", "success");
}

document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            document.getElementById('navbar_top').classList.add('fixed-top');
            // add padding top to show content behind navbar
            navbar_height = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';
        } else {
            document.getElementById('navbar_top').classList.remove('fixed-top');
            // remove padding top from body
            document.body.style.paddingTop = '0';
        }
    });
});


window.onload = function () {
    if (window.location.href.indexOf('/tienda') != -1) {
        //Hide the element.
        document.querySelectorAll('.cartSaleDiv')[0].style.display = 'inline-block';
    }
};


/**
 * Obtener csrf token por javascript
 */

function tokencsrf(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = tokencsrf('csrftoken');


// funcion que permite renderizar los botones de paypal


function initPayPalButton(total_pago) {
    //total_const = total;
    paypal.Buttons({
        style: {
            shape: 'pill',
            color: 'gold',
            layout: 'vertical',
            label: 'pay',

        },

        createOrder: function (data, actions) {
            return actions.order.create({
                purchase_units: [{
                    "amount": {
                        "currency_code": "USD",
                        "value": total_pago
                    }}
                ]
            });
        },

        onApprove: function(data) {
            //alert('Entre');
            return fetch('/carro/checkout', {
                method: 'POST',
                headers: {
                    'content-type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    orderID: data.orderID
                })
            }).then(function (res) {
                return res.json();
            }).then(function (details) {
                //alert('Transaction approved by ' + details.mensaje);
                window.location.href = "/carro/pago_completo";
            })
        },

        onError: function (err) {
            console.log('Error de Pago');
            console.log(err);
        }
    }).render('#paypal-button-container');
}

//initPayPalButton();



