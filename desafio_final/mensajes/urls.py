from django.urls import path
from . import views


urlpatterns = [
    path("inbox",views.inbox,name="inbox"),
    path("nuevo_mensaje",views.nuevo_mensaje,name="nuevo_mensaje"),
    path("borrar_mensaje/<int:id_mensaje>",views.borrar_mensaje,name="borrar_mensaje")
   
]