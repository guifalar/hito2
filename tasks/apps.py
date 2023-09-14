from django.apps import AppConfig

# Definición de la configuración de la aplicación "tasks"
class TasksConfig(AppConfig):
    
    # Campo para especificar el tipo de campo automático para las claves primarias
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación ("tasks")
    name = 'tasks'

