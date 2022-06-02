# desafio_final_repo

Este proyecto emula una cablera de una agencia de noticias en donde se accede desde http://127.0.0.1:8000/portal/ al index del sitio.

En el header está el menú que es bastante intuitivo, muestra las secciones en las que se organiza y despliega el contenido.
También está el buscador que permite encontrar noticias buscándo los términos tanto en los títulos como en las bajadas.
Además en el header está el acceso al formulario para la creación de nuevas publicaciones (noticias), nuevxs lectorxs y nuevxs periodistxs.
En el estadío actual del desarrollo ese acceso está visible para todo el mundo.

El formulario de carga de nuevas publicaciones exige el ingreso de todos los campos que están dispuestos en models.py: seccion, titulo, bajada,
nombre de quien escribe la noticia (todos estos anteriores son de texto/CharField), el correo electrónico del/la periodista (EmailField) y dos
campos mas que permiten decidir si el material se envía directo a su publicación y si además se envían al home del sitio o solo a su sección
correspondiente, en estos casos los datos son Booleans (la funcionalidad de estos campos booleanos falla porque falta apuntalar el código HTML
para que envíe los valores correspondientes según si está o no selecionado).

Además existen los formularios de carga de Lectorxs o de Periodistxs.

En cuanto a las consignas:

1- Herencia de HTML es el archivo padre.html que contiene el header, nav y footer

2- Las 3 Clases con sus respectivos Models son Noticias, Lectorxs y Periodistxs con sus respectivos Forms para la carga de los datos Nueva_noticia,
Nuevxs_Lectorxs y Nuevxs_Periodistxs

3- Como estaba descripto al incio, el acceso a cada formulario para carga de noticias, lectorxs o periodistxs está en en el menú superior
Link directo a nueva publicación
http://127.0.0.1:8000/portal/nueva_publicacion

Link directo a nuevxs usuarixs
http://127.0.0.1:8000/portal/formulario_lectorxs

Link directo a nuevxs periodistxs
http://127.0.0.1:8000/portal/formulario_periodistxs

4- El formulario de búsqueda está también en el menú de navegación por ende se muestra en todo el portal.
02/Jun/2020

