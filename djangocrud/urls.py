# Importa el módulo 'admin' de Django, que se utiliza para configurar y gestionar la interfaz de administración.
from django.contrib import admin

# Importa el módulo 'path' del paquete 'urls' de Django, que se utiliza para definir las rutas URL de la aplicación.
from django.urls import path

# Importa el módulo 'views' desde el paquete 'tasks', que contiene las vistas de la aplicación.
from tasks import views


# Definición de las rutas (URLs) de la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración de Django
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('signup/', views.signup, name='signup'),  # Ruta para el registro de usuarios
    path('tasks/', views.tasks, name='tasks'),  # Ruta para listar tareas pendientes
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),  # Ruta para listar tareas completadas
    path('tasks/create/', views.create_task, name='create_task'),  # Ruta para crear una nueva tarea
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),  # Ruta para ver detalles de una tarea
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),  # Ruta para marcar una tarea como completada
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),  # Ruta para eliminar una tarea
    path('logout/', views.signout, name='logout'),  # Ruta para cerrar sesión
    path('signin/', views.signin, name='signin')  # Ruta para iniciar sesión
]

