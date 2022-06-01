from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio,name="inicio"),
    path("inicio",views.inicio,name="inicio"),
    path("politica", views.politica ,name="politica"),
    path("economia", views.economia ,name="economia"),
    path("sociedad", views.sociedad ,name="sociedad"),
    path("deportes", views.deportes ,name="deportes"),
    path("nueva_publicacion", views.nueva_publicacion ,name="nueva_publicacion"),
    path("resultados", views.resultados ,name="resultados"),
    path("lectura", views.lectura ,name="lectura"),
    path("formulario" , views.formulario, name="formulario"),
    path("formulario_lectorxs" , views.formulario_lectorxs, name="formulario_lectorxs"),
    path("buscar" , views.buscar, name="buscar"),

]