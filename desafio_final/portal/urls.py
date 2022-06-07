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
    path("formulario_periodistxs" , views.formulario_periodistxs, name="formulario_periodistxs"),
    path("formulario_lectorxs" , views.formulario_lectorxs, name="formulario_lectorxs"),
    path("lectura/<int:id>", views.lectura ,name="lectura"),
    path("borrar_publicacion/<int:id_noticia>",views.borrar_publicacion,name="borrar_publicacion"),
    path("editar_publicacion/<int:id_noticia>",views.editar_publicacion,name="editar_publicacion"),
    path("editar_publicacion/",views.editar_publicacion,name="editar_publicacion")
]