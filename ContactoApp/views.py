from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext

from ContactoApp.Forms.forms import FormularioContacto
import datetime

def contacto(request):
    formulario = FormularioContacto()

    if request.method == "POST":
        data = request.POST
        formulario = FormularioContacto(data)
        if formulario.is_valid():
            nombre = data.get('nombre')
            email = data.get('email')
            contenido = data.get('contenido')

            #Parametrizamos los valores del correo
            today = datetime.datetime.now()
            actualDate = date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

            asunto = str("Solicitud Contacto " + nombre + " " + actualDate)
            toEmail = email
            mensaje = contenido

            try:
                send_mail(
                    asunto,
                    mensaje,
                    'django_test@gmail.com',
                    [toEmail],
                    fail_silently = False
                )
            except Exception as e:
                return HttpResponse('No se ha enviado el correo, consulte con soporte tecnico' + str(e))
            return redirect("/contacto/?valido")
        else:
            return HttpResponse('Favor revise la informacion proporcionada. Existe un error en uno o mas campos')

    return render(request, 'contacto.html', {"formContacto": formulario })