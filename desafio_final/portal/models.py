from django.db import models
from django.forms import CharField, DateField, EmailField, IntegerField

# Create your models here.

#Modelo de posteo de noticias
class Noticia(models.Model):
    seccion = models.CharField(max_length=50)
    titulo = models.CharField(max_length=140)
    bajada = models.CharField(max_length=100000)
    periodistxs = models.CharField(max_length=50)
    email_preiodistxs = models.EmailField()
    publicado = models.BooleanField()
    home = models.BooleanField()


class Lectorxs(models.Model):
    nombre_lectorxs = models.CharField(max_length=50)
    pass_lectorxs = models.CharField(max_length=50)
    email_lectorxs = models.EmailField()
    dni_lectorxs = models.IntegerField()
    nro_tarjeta_crédito = models.IntegerField()
    modo_suscripcion = models.CharField(max_length=30)

class Periodistxs(models.Model):
    nombre_periodistxs = models.CharField(max_length=50)
    sigla_periodistxs = models.CharField(max_length=10)
    pass_periodistxs = models.CharField(max_length=50)
    email_periodistxs = models.EmailField()
    dni_periodistxs = models.IntegerField()