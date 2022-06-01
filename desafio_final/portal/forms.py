from django import forms

class Nuevxs_Lectorxs(forms.Form):
    nombre_lectorxs = forms.CharField(max_length=50)
    pass_lectorxs = forms.CharField(max_length=50)
    email_lectorxs = forms.EmailField
    dni_lectorxs = forms.IntegerField()

class Nueva_noticia(forms.Form):
    seccion = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=140)
    bajada = forms.CharField(max_length=100000)
    periodistxs = forms.CharField(max_length=50)
    email_preiodistxs = forms.EmailField()


  