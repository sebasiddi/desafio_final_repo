from django.shortcuts import render
from portal.forms import Nueva_noticia, Nuevxs_Lectorxs
from django.http import HttpResponse
from portal.models import Lectorxs, Noticia
from django.template import loader

# Create your views here.

#Página de inicio
def inicio(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias}
    seccion = loader.get_template("index.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

#Secciones
def politica(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias}
    seccion = loader.get_template("1politica.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

def economia(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias}
    seccion = loader.get_template("2economia.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

def sociedad(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias}
    seccion = loader.get_template("3sociedad.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

def deportes(request):
    noticias = Noticia.objects.all()
    print(type(noticias))
    dicc = {"noticias":noticias}
    print(dicc)
    seccion = loader.get_template("4deportes.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)

# Formulario para ingresar nuevo posteo de noticias
def nueva_publicacion(request):
    if request.method == "POST":
        data_posteo = Nueva_noticia(request.POST)
        
        if data_posteo.is_valid():
            datos=data_posteo.cleaned_data
            
                        
            posteo = Noticia(seccion=datos['seccion'] ,
                            titulo = datos['titulo'],
                            bajada = datos['bajada'],
                            periodistxs = datos['periodistxs'],
                            email_preiodistxs = datos['email_preiodistxs'],
                            publicado = True,
                            home = True)
           
            
            posteo.save()
              

        
            return render(request, "index.html")
      

    return render(request, "5nueva_publicacion.html")

def resultados(request):
        if request.GET['texto']:
            texto = request.GET['texto']
            noticias = Noticia.objects.filter(bajada__icontains = texto) or Noticia.objects.filter(titulo__icontains = texto)
            return render (request,"6resultados.html",{"noticias":noticias})
        else:
            return HttpResponse("Campo vacío")
    

def lectura(request):
    return render(request,"7lectura.html")


def formulario(request):
    """
    if request.method == "POST":
        
        mi_formulario = Nueva_publicacion(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso = Noticia(titulo=datos['titulo'])
            curso.save()
            return render(request, "formulario.html")
    """
    return render(request,"formulario.html")

    
def formulario_lectorxs(request):
    if request.method == "POST":
        
        mi_formulario = Nuevxs_Lectorxs(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso = Lectorxs(nombre_lectorxs=datos['nombre_lectorxs'],pass_lectorxs=datos['pass_lectorxs'],dni_lectorxs=datos['dni_lectorxs'])
            curso.save()
            return render(request, "formulario_lectorxs.html")
        return render(request,"6resultados.html")
    return render(request,"formulario_lectorxs.html")

def buscar(request):
    return render(request, "buscar.html")
