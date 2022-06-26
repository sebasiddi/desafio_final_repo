from django.shortcuts import render
from portal.models import Avatar
from portal.views import dicc
from mensajes.models import Mensaje
from mensajes.forms import Nuevo_mensaje
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def inbox(request):
    data_mensajes = Mensaje.objects.all()
    avatares = Avatar.objects.all()
    data = {"users":avatares,"mensajes":data_mensajes[::-1]}
    data.update(dicc(request))
    return render(request,"mensajesportal.html",data)

def nuevo_mensaje(request):
    if request.method == "POST":
        data_mensaje = Nuevo_mensaje(request.POST)

        if data_mensaje.is_valid():
            datos = data_mensaje.cleaned_data
           
            user = Avatar.objects.filter(user=request.user.id)


            mensaje = Mensaje(
                        id_envia = user[0].user_id,
                        id_recibe = datos["id_recibe"],
                        titulo_mensaje = datos["titulo_mensaje"],
                        cuerpo_mensaje = datos["cuerpo_mensaje"],
                        fecha_mensaje = datetime.now())
            mensaje.save()
            avatares = Avatar.objects.all()
            data = {"users":avatares}
            data.update(dicc(request))
            return render(request,"mensajesportal.html",data)
    else:
        avatares = Avatar.objects.all()
        data = {"users":avatares}
        data.update(dicc(request))
        return render(request,"nuevo_mensaje.html",data)     

#Borrar mensaje
@login_required
def borrar_mensaje(request,id_mensaje):
    mensaje_para_borrar = Mensaje.objects.get(id=id_mensaje)
    mensaje_para_borrar.delete()
    data_mensajes = Mensaje.objects.all()
    avatares = Avatar.objects.all()
    data = {"users":avatares,"mensajes":data_mensajes[::-1]}
    data.update(dicc(request))
    return render(request, "mensajesportal.html",data)