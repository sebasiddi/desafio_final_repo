from ast import Pass
from datetime import datetime
from time import timezone
from turtle import home
from django.shortcuts import render
from portal.forms import Nueva_noticia, User_Edit_Form
from portal.models import Noticia, Avatar
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

#Función que carga en un diccionario la DB para mostrar en diferentes páginas del sitio
#Se carga la lista de noticias completa, la lista de noticias que va a la marquesina de "Últimos Títulos" y la lista que va al carousel
#y los datos y avatar de quien se haya loggeado, la llamo para enviar el diccionario generado en cada return
def dicc(request):
    noticias= Noticia.objects.all()
    noticias_titulos=noticias[::-1]
    noticias_home=[]
    for n in noticias_titulos:
        if n.home == 1:
            noticias_home.append(n)
    n1 = noticias_home[0]
    n2 = noticias_home[1]
    n3 = noticias_home[2]
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return ({"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5],"noticia1":n1,"noticia2":n2,"noticia3":n3,"url":avatares[0].imagen.url})
    else:
        return ({"noticias":noticias[::-1], "noticias_titulos":noticias_titulos[0:5],"noticia1":n1,"noticia2":n2,"noticia3":n3,"url":"/media/avatares/basico.png"})

#Página de bienvenida
def home(request):
    return render(request, "home.html",dicc(request))

#Página de inicio
def inicio(request):
    return render(request, "index.html",dicc(request))
    
@login_required
#Muestro las publicaciones hechas por quien se haya loggeado
def mis_publicaciones(request):
    mis_noticias=Noticia.objects.filter(id_user__exact = request.user.id)
    data=(dicc(request))
    data.update({"mis_noticias":mis_noticias[::-1]})
    return render(request, "mis_publicaciones.html",data)


#Secciones
@login_required
def politica(request):
    return render(request, "1politica.html",dicc(request))
    
    
@login_required
def economia(request):
    return render(request, "2economia.html",dicc(request))

@login_required
def sociedad(request):
    return render(request, "3sociedad.html",dicc(request))

@login_required
def deportes(request):
    return render(request, "4deportes.html",dicc(request))

# Formulario para ingresar nuevo posteo de noticias
@login_required
def nueva_publicacion(request):
    if request.method == "POST":

        data_posteo = Nueva_noticia(request.POST,request.FILES)
        print(data_posteo)
        if data_posteo.is_valid():
            datos=data_posteo.cleaned_data
            #chequeo de cómo llega la información boolean desde el form
            print(datos["publicado"])
            posteo = Noticia(seccion=datos['seccion'] ,
                            titulo = datos['titulo'],
                            bajada = datos['bajada'],
                            cuerpo = datos['cuerpo'],
                            fecha = datetime.now(),
                            img = datos['img'],
                            nombre_user = datos['nombre_user'],
                            id_user = datos['id_user'],
                            publicado = datos['publicado'],
                            home = datos['home'])
            posteo.save() 
            return render(request, "index.html",dicc(request))
        else:
            print("data posteo no es valido")
    return render(request, "5nueva_publicacion.html",dicc(request)) 


#Búsqueda
@login_required
def resultados(request):
        avatares = Avatar.objects.filter(user=request.user.id)
        if request.GET['texto']:
            texto = request.GET['texto']
            # Búsqueda por Título y contenido de la noticia
            noticias = Noticia.objects.filter(bajada__icontains = texto) or Noticia.objects.filter(titulo__icontains = texto) or Noticia.objects.filter(cuerpo__icontains = texto)
            if avatares.exists():
                return render(request, "6resultados.html",{"noticias":noticias[::-1], "url":avatares[0].imagen.url})
            else:
                return render (request,"6resultados.html",{"noticias":noticias[::-1]})
        else:
            if avatares.exists():
                return render(request, "6resultados.html",{"url":avatares[0].imagen.url})
            else:
                return render (request,"6resultados.html")

#Lectura de noticias mediante link en título
def lectura(request,id):
    noticia_lectura = Noticia.objects.filter(id__exact = id)
    avatares = Avatar.objects.filter(user=request.user.id)
    data = dicc(request)
    data.update({"noticia_lectura":noticia_lectura})
    return render(request, "7lectura.html",data)

 
#Borrar publicaciones
@login_required
def borrar_publicacion(request,id_noticia):
    noticia_para_borrar = Noticia.objects.get(id=id_noticia)
    noticia_para_borrar.img.delete(False)
    noticia_para_borrar.delete()
    return render(request, "index.html",dicc(request))



#Editar publicaciones
#@login_required
def editar_publicacion(request,id_noticia):
    noticia_para_editar = Noticia.objects.get(id=id_noticia)
    if request.method == "POST":
        formulario_publicacion = Nueva_noticia(request.POST,request.FILES)
        if formulario_publicacion.is_valid():
            datos = formulario_publicacion.cleaned_data
            noticia_para_editar.seccion=datos['seccion']
            noticia_para_editar.titulo = datos['titulo']
            noticia_para_editar.bajada = datos['bajada']
            noticia_para_editar.cuerpo = datos['cuerpo']
            noticia_para_editar.fecha = datetime.now()
            noticia_para_editar.img.delete(False)
            noticia_para_editar.img = datos['img']
            noticia_para_editar.nombre_user = datos['nombre_user']
            noticia_para_editar.id_user = datos['id_user']
            noticia_para_editar.publicado = datos['publicado']
            noticia_para_editar.home = datos['home']
            noticia_para_editar.save()
            render(request, "index.html",dicc(request))
    else:
        formulario_publicacion = Nueva_noticia(initial={'seccion':noticia_para_editar.seccion,'titulo':noticia_para_editar.titulo,'bajada':noticia_para_editar.bajada,'cuerpo':noticia_para_editar.cuerpo,'fecha':datetime.now(),'img':noticia_para_editar.img,'nombre_user':noticia_para_editar.nombre_user,'id_user':noticia_para_editar.id_user,'publicado':noticia_para_editar.publicado,'home': noticia_para_editar.home})
    data = dicc(request)
    data.update({"formulario_publicacion":formulario_publicacion ,"noticia_para_editar":noticia_para_editar})
    return render(request, "editar_publicacion.html",data) 





# Login con formulario de django
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "index.html", dicc(request))
            else:
                data=dicc(request)
                data.update({"mensaje":"Usuario Incorrecto",'form':form})  
                return render(request,"login.html",data)
        else:
            data=dicc(request)
            data.update({"mensaje":"Error",'form':form})  
            return render(request,"login.html",data) 
    
    form = AuthenticationForm()
    data=dicc(request)
    data.update({'form':form})  
    return render(request,"login.html",data)
    


#Alta de nuevxs usuarixs
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthenticationForm()
            data=dicc(request)
            data.update({'mensaje':'Registro Exitoso','form':form})  
            request.method = "GET"
            return render(request,"login.html",data)
    else:
        form = UserCreationForm()
    data=dicc(request)
    data.update({"form":form})
    return render (request, "registro.html",data)


# Editar el perfi: cambio mail y/o contraseña
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
                return render(request, "index.html",dicc(request))
    else:
        miFormulario = User_Edit_Form ( initial = {'email':usuario.email} )
        
    data = dicc(request)
    data.update({"miFormulario":miFormulario,"usuario":usuario})
    return render(request,"editar_perfil.html",data)




# Cambio de imagen de perfil/avatar
@login_required
def cambiar_avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        perfil = Avatar(id=avatares[0].id,
                        user=avatares[0].user,
                        imagen=request.FILES['imagen'])
        perfil.save()
        return render(request, "index.html",dicc(request))
    else:
        perfil = Avatar(id=request.user.id,
                        user=request.user,
                        imagen=request.FILES['imagen'])
        perfil.save()
        return render(request, "index.html",dicc(request))

# Acerca De
def about(request):
    return render(request,"about.html",dicc(request))
    



""" ESTO ES DE LA ENTREGA PREVIA Y QUEDA EN DESUSO PERO LO QUIERO CONSERVAR 
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
"""