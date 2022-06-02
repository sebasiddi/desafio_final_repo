from turtle import home
from django.shortcuts import render
from portal.forms import Nueva_noticia, Nuevxs_Lectorxs, Nuevxs_Periodistxs
from django.http import HttpResponse
from portal.models import Noticia, Lectorxs, Periodistxs
from django.template import loader

# Create your views here.

#Página de inicio
def inicio(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias[::-1]}
    seccion = loader.get_template("index.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

#Secciones
def politica(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias[::-1]}
    seccion = loader.get_template("1politica.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

def economia(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias[::-1]}
    seccion = loader.get_template("2economia.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

def sociedad(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias[::-1]}
    seccion = loader.get_template("3sociedad.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

def deportes(request):
    noticias = Noticia.objects.all()
    print(type(noticias))
    dicc = {"noticias":noticias[::-1]}
    seccion = loader.get_template("4deportes.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

# Formulario para ingresar nuevo posteo de noticias
def nueva_publicacion(request):
    if request.method == "POST":
        data_posteo = Nueva_noticia(request.POST)
        if data_posteo.is_valid():
            datos=data_posteo.cleaned_data
            
            #chequeo de cómo llega la información boolean desde el form
            #print("Form publicado:",datos['publicado'],"Home:",datos['home'])    
                        
            posteo = Noticia(seccion=datos['seccion'] ,
                            titulo = datos['titulo'],
                            bajada = datos['bajada'],
                            periodistxs = datos['periodistxs'],
                            email_preiodistxs = datos['email_preiodistxs'],
                            publicado = datos['publicado'],
                            home = datos['home'])
           
            posteo.save()
             
            return render(request, "index.html")
     
    return render(request, "5nueva_publicacion.html")


#Formulario para alta de lectorxs
def formulario_lectorxs(request):
   
    if request.method == "POST":
        
        form_l = Nuevxs_Lectorxs(request.POST)
        if form_l.is_valid():
            datos=form_l.cleaned_data
            alta_lectorxs = Lectorxs(nombre_lectorxs=datos['nombre_lectorxs'],
                             pass_lectorxs=datos['pass_lectorxs'],
                             email_lectorxs = datos['email_lectorxs'],
                             dni_lectorxs=datos['dni_lectorxs'],
                             nro_tarjeta_crédito =datos['nro_tarjeta_crédito'],
                             modo_suscripcion = datos['modo_suscripcion'],)
            alta_lectorxs.save()
            return render(request, "index.html")
        return render(request,"index.html")
    
    return render(request,"formulario_lectorxs.html")


#Formulario para alta de periodistxs
def formulario_periodistxs(request):
    
    if request.method == "POST":
        
        form_p = Nuevxs_Periodistxs(request.POST)
        if form_p.is_valid():
            
            datos=form_p.cleaned_data
            alta_periodistxs = Periodistxs(nombre_periodistxs=datos['nombre_periodistxs'],
                                           sigla_periodistxs=datos['sigla_periodistxs'],
                                           pass_periodistxs=datos['pass_periodistxs'],
                                           email_periodistxs = datos['email_periodistxs'],
                                           dni_periodistxs=datos['dni_periodistxs'],)
            alta_periodistxs.save()
            return render(request, "index.html")
        else:
            print("falla en el form")
        return render(request,"index.html")
    
    return render(request,"formulario_periodistxs.html")




#Búsqueda


def resultados(request):
        if request.GET['texto']:
            texto = request.GET['texto']

            # Búsqueda por Título y contenido de la noticia

            noticias = Noticia.objects.filter(bajada__icontains = texto) or Noticia.objects.filter(titulo__icontains = texto)
            return render (request,"6resultados.html",{"noticias":noticias[::-1]})
        else:
            return render (request,"6resultados.html")
    
#Lectura de noticias mediante link en título (Work in Progress)
def lectura(request,id):
        noticias = Noticia.objects.filter(id__icontains = id)
        return render (request,"7lectura.html",{"noticias":noticias})