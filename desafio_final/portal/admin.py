from django.contrib import admin

from portal.models import Noticia, Periodistxs, Lectorxs

# Register your models here.
admin.site.register(Noticia)

admin.site.register(Lectorxs)

admin.site.register(Periodistxs)