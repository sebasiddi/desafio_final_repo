# desafio_final_repo Agencia de Noticias

Este proyecto emula una cablera de una agencia de noticias en donde se accede desde /portal/ al index del sitio.

En el header está el menú que es bastante intuitivo, muestra las secciones en las que se organiza y despliega el contenido. También está el buscador que permite encontrar noticias buscándo los términos tanto en los títulos como en las bajadas.
Además en el header está el acceso al formulario para la creación de nuevas publicaciones (noticias). En el estadío actual del desarrollo ese acceso está visible para todo el mundo.

El formulario de carga de nuevas publicaciones exige el ingreso de todos los campos que están dispuestos en models.py: seccion, titulo, bajada, nombre de quien escribe la noticia (todos estos anteriores son de texto/CharField), el correo electrónico del/la periodista (EmailField) y dos checkboxes que permiten decidir si el material se envía directo a su publicación y si además se envían al home del sitio o solo a su sección correspondiente, en estos casos los datos son Booleans.




