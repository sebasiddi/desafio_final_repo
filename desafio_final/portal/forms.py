from django import forms

class Nueva_noticia(forms.Form):
    seccion = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=140)
    bajada = forms.CharField(max_length=100000)
    periodistxs = forms.CharField(max_length=50)
    email_preiodistxs = forms.EmailField()
    publicado = forms.BooleanField()
    home = forms.BooleanField()


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


  