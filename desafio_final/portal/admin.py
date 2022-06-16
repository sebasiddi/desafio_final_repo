from django.contrib import admin

from portal.models import Avatar, Lectorxs, Noticia, Periodistxs

# Register your models here.
admin.site.register(Noticia)

admin.site.register(Lectorxs)

admin.site.register(Periodistxs)

admin.site.register(Avatar)
