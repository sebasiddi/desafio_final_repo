from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    id_envia = models.IntegerField()
    id_recibe = models.IntegerField()
    titulo_mensaje = models.CharField(max_length=50)
    cuerpo_mensaje = models.CharField(max_length=3000)
    fecha_mensaje = models.DateTimeField()