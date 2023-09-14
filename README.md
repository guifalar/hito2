# hito2
Trabajo Practico Argentina Programa
Pasos para la creacion de Aplicacion para gestion de tareas en Django


Creo la carpeta DJANGO-CRUD

Creo un entorno virtual: pip install virtualenv

python –m venv venv

lo activo ejecutando backend\Scripts\active.bat (en visual estudio F1, interprete phyton y elijo el sugerido.
Es posible que tenga que reiniciar el terminal.

Instalo Django: pip install django

Creo el proyecto: django-admin startproject djangocrud .(es importante dejar un espacio entre django 
y el punto para que cree la carpeta del proyecto al mismo nivel que la carpeta del entorno virtual.

Creo la aplicacion: Python manage.py startapp task

Agrego en diangocrud/settings el nombre de la app creada: tasks

Ejecuto para probar y para que se cree la base de datos: python manage.py runserver

Creo el formulario signup, para registrar a los usuarios. 
En el archivo task/views.py defino la vista (funcion) signup y realizo el codigo para su funcionamiento
En la carpeta task/templates creo la pagina signup.html que contiene el formulario de registro.
En el archivo djangocrud/urls.py defino la ruta de signup
  
genero las tablas para ingresar los datos de signup (registro): python manage.py migrate


Sigo la misma logica para todas las vistas: 
creo la vista en task/views.py
creo en task/templates cada una de las paginas html
creo en djangocrud/urls.py las rutas


Creo en tasks/models.py la estructura de la tabla task

ejecuto para que se cree el codigo para crear la tabla en la base de datos: python manage.py makemigrations

ejecuto para que se cree efectivamente en la base de datos: python manage.py migrate



En tasks/form.py defino la estructura del formulario para crear la gestion de tareas
