# Importa el módulo 'admin' de Django, que se utiliza para configurar y gestionar la interfaz de administración.
from django.contrib import admin

# Importa el modelo 'Task' desde el módulo local '.models'. 
# El modelo 'Task' está definido en un archivo llamado 'models.py'.
from .models import Task


# Definir una clase personalizada para la administración de tareas (TaskAdmin)
class TaskAdmin(admin.ModelAdmin):
    
    # Definir campos de solo lectura en la página de detalles de tareas
    readonly_fields = ("created",)
    
# Registrar el modelo "Task" en el panel de administración de Django utilizando la clase personalizada TaskAdmin
admin.site.register(Task, TaskAdmin)

