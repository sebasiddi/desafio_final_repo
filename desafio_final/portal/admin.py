from django.contrib import admin

from portal.models import Avatar, Lectorxs, Noticia, Periodistxs, Imagen_post

# Register your models here.
admin.site.register(Noticia)

admin.site.register(Lectorxs)

admin.site.register(Periodistxs)

admin.site.register(Avatar)

admin.site.register(Imagen_post)
