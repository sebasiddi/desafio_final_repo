from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, DateField, EmailField, IntegerField
from django.contrib.auth.models import User

# Create your models here.

#Modelo de posteo de noticias
class Noticia(models.Model):
    seccion = models.CharField(max_length=50)
    titulo = models.CharField(max_length=140)
    bajada = models.CharField(max_length=10000)
    cuerpo = models.CharField(max_length=30000)
    fecha = models.DateTimeField()
    img = models.ImageField(upload_to='img/', null=True ,blank=True )
    nombre_user = models.CharField(max_length=50)
    id_user = models.IntegerField()
    publicado = models.BooleanField()
    home = models.BooleanField()

    def __str__(self):
            return f"ID: {self.id} | Sección: {self.seccion} - Título: {self.titulo}"


class Lectorxs(models.Model):
    nombre_lectorxs = models.CharField(max_length=50)
    pass_lectorxs = models.CharField(max_length=50)
    email_lectorxs = models.EmailField()
    dni_lectorxs = models.IntegerField()
    nro_tarjeta_crédito = models.IntegerField()
    modo_suscripcion = models.CharField(max_length=30)


    def __str__(self):
            return f"ID: {self.id} Nombre: {self.nombre_lectorxs}, E-mail: {self.email_lectorxs}"

class Periodistxs(models.Model):
    nombre_periodistxs = models.CharField(max_length=50)
    sigla_periodistxs = models.CharField(max_length=10)
    pass_periodistxs = models.CharField(max_length=50)
    email_periodistxs = models.EmailField()
    dni_periodistxs = models.IntegerField()

    def __str__(self):
            return f"ID: {self.id} - Nombre: {self.nombre_periodistxs}, E-mail: {self.email_periodistxs}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True ,blank=True )

    def __str__(self) -> str:
          return f"ID: {self.id}, User: {self.user}"
          
class Imagen_post(models.Model):
    id_post = models.IntegerField()
    imagen = models.ImageField(upload_to='img', null=True ,blank=True )