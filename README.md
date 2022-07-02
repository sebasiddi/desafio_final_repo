# desafio_final_repo
Este trabajo final fue desarrollado completamente por Sebastian Siddi a excepción de la plantilla descargada para contener el sitio.
De todos modos también se modificaron algunos detalles de CSS y se utilizó también herramientas de Bootstrap para el front.

Para este proyecto final trabajé sobre la pre-entrega en donde presenté un sitio que emula una cablera de una agencia de noticias.

Si bien en una agencia de noticias quienes acceden al sitio no tienen la posibilidad de registrarte y generar contenido, en este caso sí es posible en función de cumplir con las consignas de esta entrega final lo que lo hace tener un funcionamiento similar al de un blog.

Hay en el código y en la DB contenido que es obsoleto heredado de la entrega anterior pero que decidí deliveradamente no elminiar para el caso de querer continuarlo en un futuro. Nada de eso está accesible al usuario.

En cuanto al sitio presentado, en el header heredado está el menú que es bastante intuitivo, muestra las secciones en las que se organiza y despliega el contenido además de las opciones de registro, loggeo, etc.
También está el buscador que permite encontrar noticias buscándo los términos tanto en los títulos como en las bajadas y cuerpo de las noticias.

El formulario de carga de nuevas publicaciones exige el ingreso de algunos de los campos que están dispuestos en models.py: seccion, titulo, bajada/copete, cuerpo de la noticia e imagen ilustrativa. Ademas hay dos campos que permiten decidir si el material se envía directo a su publicación y si además se envían al home del sitio o solo a su sección. Otros de los campos del modelo se completan automáticamente desde el código, como por ejemplo la fecha de creación de las publicaciones.

En cuanto a las consignas:

-El sitio tiene un home de bienvenida a lxs usuarixs en el que se puede elegir acceder a las noticias (página de inicio) o al loggeo directamente (en caso de estar ya loggeado envía a la edición de perfil)

-En el inicio del portal de noticias se despliega la lista de entradas en general (a excepción de las que deliveradamente no se hayan enviado a publicar al home al momento de crearlas o editarlas.)

-Cada usuario registrado tiene la posibilidad de crear contenido, también puede editar solo sus propias publicaciones, para ayudar a eso en el menú superior está la opción de ver "Mis publicaciones" y allí se listan solo las que haya creado cada usuario

-desde http://127.0.0.1:8000/ se accede directamente al home

-Tanto en inicio como en las diferentes secciones se puede acceder a una vista previa de la noticia en donde de muestra el título, bajada y la foto en un tamaño pequeño

-para el registro de usuarixs utilicé lo visto en clase, se genera un nombre de usuario y contraseña, luego en editar perfil se puede agregar y/o modificar una cuenta de e-mail, también se puede cambiar el avatar que se asigna por defecto.

-el usuario admin es superuser y su password es codercoder

-se creó una app de menasajes que administra la mensajería interna entre usuarixs con bandeja de entrada y bandeja de mensajes enviados.

Video de captura del sitio funcionando

[![Alt text](https://img.youtube.com/vi/1JpqgLZHccw/0.jpg)](https://www.youtube.com/watch?v=1JpqgLZHccw)


01/Jul/2022



