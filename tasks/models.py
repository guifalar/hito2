# Importar los módulos necesarios

# Importa el módulo 'models' de Django, que se utiliza para definir modelos de base de datos.
from django.db import models

# Importa el modelo 'User' del módulo 'auth' de Django, que gestiona la autenticación de usuarios.
from django.contrib.auth.models import User


# Definición de modelos en Django

class Task(models.Model):
    # Definición de campos para el modelo "Task"

    # Campo de texto para el título de la tarea, con un límite de 100 caracteres
    title = models.CharField(max_length=100, verbose_name="Título")

    # Campo de texto largo para la descripción de la tarea (puede estar en blanco)
    description = models.TextField(blank=True, verbose_name="Descripción") 

    # Campo de fecha y hora que se autocompleta con la fecha y hora actual cuando se crea la tarea
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    # Campo de fecha y hora que puede ser nulo (para tareas no completadas)
    datecompleted = models.DateTimeField(null=True, verbose_name="Fecha de Completado")

    # Campo booleano para indicar si la tarea es importante o no (valor predeterminado: False)
    important = models.BooleanField(default=False, verbose_name="Importante")

    # Relación con el modelo de usuario incorporado de Django (User)
    # Se utiliza ForeignKey para relacionar cada tarea con un usuario específico, y on_delete=models.CASCADE
    # indica que si se elimina el usuario, también se deben eliminar sus tareas asociadas
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    # Método para representar una tarea como una cadena de texto legible
    def __str__(self):
        # Devuelve el título de la tarea seguido por el nombre de usuario del propietario
        return self.title + '- por ' + self.user.username
