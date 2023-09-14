# Importa 'ModelForm' desde el módulo 'forms' de Django, que se utiliza para crear formularios basados en modelos.
from django.forms import ModelForm

# Importa el modelo 'Task' desde el módulo local '.models'. 
# El modelo 'Task' está definido en un archivo llamado 'models.py'.
from .models import Task


# Definir un formulario basado en el modelo "Task"
class TaskForm(ModelForm):
    class Meta:
        # Especificar el modelo en el que se basará el formulario
        model = Task

        # Definir los campos del modelo que estarán disponibles en el formulario
        fields = ['title', 'description', 'important']
