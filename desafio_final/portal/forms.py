from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Nueva_noticia(forms.Form):
    seccion = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=140)
    bajada = forms.CharField(max_length=10000)
    cuerpo = forms.CharField(max_length=30000)
    #fecha = forms.DateField()
    img = forms.ImageField()
    nombre_user = forms.CharField(max_length=50)
    id_user = forms.IntegerField()
    publicado = forms.IntegerField()
    home = forms.IntegerField()

class User_Edit_Form(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1: forms.Field(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.Field(label="Repetir la contraseña",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_texto = {k:"" for k in fields}

class Nuevxs_Lectorxs(forms.Form):
    nombre_lectorxs = forms.CharField(max_length=50)
    pass_lectorxs = forms.CharField(max_length=50)
    email_lectorxs = forms.EmailField()
    dni_lectorxs = forms.IntegerField()
    nro_tarjeta_crédito = forms.IntegerField()
    modo_suscripcion = forms.CharField(max_length=30)

    
class Nuevxs_Periodistxs(forms.Form):
    nombre_periodistxs = forms.CharField(max_length=50)
    sigla_periodistxs = forms.CharField(max_length=10)
    pass_periodistxs = forms.CharField(max_length=50)
    email_periodistxs = forms.EmailField()
    dni_periodistxs = forms.IntegerField()
