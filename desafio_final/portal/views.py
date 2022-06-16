from ast import Pass
from turtle import home
from django.shortcuts import render
from portal.forms import Nueva_noticia, Nuevxs_Lectorxs, Nuevxs_Periodistxs, User_Edit_Form
from django.http import HttpResponse
from portal.models import Noticia, Lectorxs, Periodistxs, Avatar
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#Página de inicio
"""
def inicio(request):
    noticias = Noticia.objects.all()
    dicc = {"noticias":noticias[::-1]}
    seccion = loader.get_template("index.html")
    documento=seccion.render(dicc)
    return HttpResponse(documento)
"""

def home(request):
    return render(request, "home.html")


def inicio(request):
    noticias= Noticia.objects.all()
    noticias_titulos=noticias[::-1]
    return render(request, "index.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5]})


#Secciones
@login_required
def politica(request):
    noticias= Noticia.objects.all()
    noticias_titulos=noticias[::-1]
    return render(request, "1politica.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5]})


@login_required
def economia(request):
    noticias= Noticia.objects.all()
    noticias_titulos=noticias[::-1]
    return render(request, "2economia.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5]})

@login_required
def sociedad(request):
    noticias= Noticia.objects.all()
    noticias_titulos=noticias[::-1]
    return render(request, "3sociedad.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5]})

@login_required
def deportes(request):
    noticias= Noticia.objects.all()
    noticias_titulos=noticias[::-1]
    return render(request, "4deportes.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5]})

# Formulario para ingresar nuevo posteo de noticias
@login_required
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
            noticias=Noticia.objects.all()

            return render (request, "index.html" , {"noticias":noticias[::-1]})
     
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
            noticias=Noticia.objects.all()

            return render (request, "index.html" , {"noticias":noticias[::-1]})
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
            noticias=Noticia.objects.all()

            return render (request, "index.html" , {"noticias":noticias[::-1]})
     
        return render(request,"index.html")
    
    return render(request,"formulario_periodistxs.html")


#Búsqueda
@login_required
def resultados(request):
        if request.GET['texto']:
            texto = request.GET['texto']
            # Búsqueda por Título y contenido de la noticia
            noticias = Noticia.objects.filter(bajada__icontains = texto) or Noticia.objects.filter(titulo__icontains = texto)
            return render (request,"6resultados.html",{"noticias":noticias[::-1]})
        else:
            return render (request,"6resultados.html")
    
#Lectura de noticias mediante link en título (Work in Progress)
@login_required
def lectura(request,id):
        noticias = Noticia.objects.filter(id__exact = id)
        return render (request,"7lectura.html",{"noticias":noticias})

#Borrar publicaciones
@login_required
def borrar_publicacion(request,id_noticia):
    noticia_para_borrar = Noticia.objects.get(id=id_noticia)
    noticia_para_borrar.delete()
    noticias=Noticia.objects.all()
    return render (request, "index.html" , {"noticias":noticias[::-1]})

#Editar publicaciones
#@login_required
def editar_publicacion(request,id_noticia):
    noticia_para_editar = Noticia.objects.get(id=id_noticia)
    if request.method == "POST":
        formulario_publicacion = Nueva_noticia(request.POST)
        
        
        if formulario_publicacion.is_valid():
            
            datos = formulario_publicacion.cleaned_data
        
            noticia_para_editar.seccion=datos['seccion']
            noticia_para_editar.titulo = datos['titulo']
            noticia_para_editar.bajada = datos['bajada']
            noticia_para_editar.periodistxs = datos['periodistxs']
            noticia_para_editar.email_preiodistxs = datos['email_preiodistxs']
            noticia_para_editar.publicado = datos['publicado']
            noticia_para_editar.home = datos['home']
            noticia_para_editar.save()
            noticias = Noticia.objects.all() 
            return render(request, "index.html",{"noticias":noticias[::-1]})
    
    else:
        formulario_publicacion = Nueva_noticia(initial={'seccion':noticia_para_editar.seccion,'titulo':noticia_para_editar.titulo,'bajada':noticia_para_editar.bajada,'periodistxs':noticia_para_editar.periodistxs,'email_preiodistxs':noticia_para_editar.email_preiodistxs,'publicado':noticia_para_editar.publicado,'home': noticia_para_editar.home})

    return render(request,"editar_publicacion.html",{"formulario_publicacion":formulario_publicacion ,"noticia_para_editar":noticia_para_editar})

def edit(request,id_noticia):
    noticia_editar = Noticia.objects.get(id=id_noticia)
    if request.method == "POST":
        miFormulario = Nueva_noticia(request.POST)
        print(miFormulario)    

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            noticia_editar.seccion = informacion['seccion']
            noticia_editar.titulo = informacion['titulo']
            noticia_editar.bajada = informacion['bajada']
            noticia_editar.periodistxs = informacion['periodistxs']
            noticia_editar.email_preiodistxs = informacion['email_preiodistxs']
            noticia_editar.publicado = informacion['publicado']
            noticia_editar.home = informacion['home']
            noticia_editar.save()

            return render(request,"inicio.html")
    else:
        miFormulario=Nueva_noticia(initial={'seccion':noticia_editar.seccion,'titulo':noticia_editar.titulo,'bajada':noticia_editar.bajada,'periodistxs':noticia_editar.periodistxs,'email_preiodistxs':noticia_editar.email_preiodistxs,'publicado':noticia_editar.publicado,'home':noticia_editar.home,})
    
    return render(request,'edit.html',{"miFormulario":miFormulario,"noticia_editar":noticia_editar})
    
    
############# LOGIN

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                noticias=Noticia.objects.all()
                noticias=Noticia.objects.all()
                noticias_titulos=noticias[::-1]
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares.exists():
                    print(avatares[0].imagen.url)
                    return render(request, "index.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5],"url":avatares[0].imagen.url})
                else:
                    return render(request, "index.html",{"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5]})
            else:
                return render(request,"index.html",{"mensaje","Error, datos incorrectos"})
        else:
            return render(request,"index.html",{"mensaje":"Error, formulario incorrecto"})
    
    form = AuthenticationForm()
   
    return render(request,"login.html",{'form':form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("usuario creado")

    else:
        form = UserCreationForm()
    
    return render (request, "registro.html",{"form":form})


@login_required
def editar_perfil(request):
    
    usuario=request.user
    
    if request.method == 'POST':
            miFormulario=User_Edit_Form(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data

                usuario.email = informacion['email']
                password = informacion['password1']
                usuario.set_password(password)
                usuario.save()

                return render(request,"index.html")
    else:
        miFormulario = User_Edit_Form ( initial = {'email':usuario.email} )
        avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,"editar_perfil.html",{"miFormulario":miFormulario,"usuario":usuario,"url":avatares[0].imagen.url})

    