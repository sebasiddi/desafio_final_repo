from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Nuevo_mensaje(forms.Form):
    id_recibe = forms.IntegerField()
    titulo_mensaje = forms.CharField(max_length=50)
    cuerpo_mensaje = forms.CharField(max_length=3000)
