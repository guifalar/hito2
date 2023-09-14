# Importación de módulos necesarios
from django.shortcuts import render, redirect, get_object_or_404
# Importaciones relacionadas con vistas y redirecciones:
# - 'render' se utiliza para renderizar plantillas HTML.
# - 'redirect' se utiliza para redirigir a otras páginas.
# - 'get_object_or_404' se usa para obtener un objeto o mostrar una página 404 si no se encuentra.

from django.http import HttpResponse
# Importación para HttpResponse, que se utiliza para devolver respuestas HTTP personalizadas.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Importaciones relacionadas con formularios de autenticación:
# - 'UserCreationForm' es un formulario predeterminado para el registro de usuarios.
# - 'AuthenticationForm' es un formulario predeterminado para la autenticación de usuarios.

from django.contrib.auth.models import User
# Importación del modelo 'User' de Django, que se utiliza para trabajar con usuarios.

from django.contrib.auth import login, logout, authenticate
# Importaciones relacionadas con la autenticación de usuarios:
# - 'login' se usa para iniciar sesión de usuarios.
# - 'logout' se utiliza para cerrar la sesión de usuarios.
# - 'authenticate' se usa para autenticar usuarios.

from django.db import IntegrityError
# Importación de IntegrityError, que se usa para manejar errores de integridad en la base de datos.

from .form import TaskForm
# Importación del formulario personalizado 'TaskForm' desde el directorio actual.

from .models import Task
# Importación del modelo 'Task' desde el directorio actual.

from django.utils import timezone
# Importación de 'timezone' para trabajar con zonas horarias y fechas y horas.

from django.contrib.auth.decorators import login_required
# Importación de 'login_required' para aplicar decoradores de autenticación en vistas.


# Vistas de Django

# Vista para la página de inicio (home)
def home(request):
    return render(request, 'home.html')

# Vista para registrar un nuevo usuario (signup)
def signup(request):
    if request.method == 'GET':
        # Si la solicitud HTTP es de tipo GET, renderizar el formulario de registro (signup.html)
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        # Si la solicitud es de tipo POST (envío de formulario)
        if request.POST['password1'] == request.POST['password2']:
            # Verificar si las contraseñas coinciden

            try:
                # Intentar crear un nuevo usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], 
                                                first_name=request.POST['first_name'], email=request.POST['email'])
                user.save()
                # Iniciar sesión para el nuevo usuario
                login(request, user)
                return redirect('tasks')  # Redirigir a la página de tareas
            except IntegrityError:
                # Si hay un error de integridad (nombre de usuario duplicado), mostrar un mensaje de error
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'El nombre de usuario ya existe'
                })
        else:
            # Si las contraseñas no coinciden, mostrar un mensaje de error
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden'
            })
        


# Vista para listar tareas pendientes (tasks)
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks': tasks})

# Vista para listar tareas completadas (tasks_completed)
@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'tasks_completed.html', {'tasks': tasks})

# Vista para crear una nueva tarea (create_task)
@login_required
def create_task(request):
    if request.method == 'GET':
        # Si la solicitud HTTP es de tipo GET, renderizar el formulario de creación de tarea
        return render(request, 'create_task.html', {
            'form': TaskForm()
        })
    else:
        # Si la solicitud es de tipo POST (envío de formulario)
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')  # Redirigir a la lista de tareas
        except ValueError:
            # Si hay un error en la validación de datos, mostrar un mensaje de error
            return render(request, 'create_task.html', {
                'form': TaskForm(),
                'error': 'Por favor ingrese datos válidos'
            })

# Vista para ver y editar detalles de una tarea (task_detail)
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')  # Redirigir a la lista de tareas
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form,
                                                        'error': 'Error en la actualización de tareas'})

# Vista para marcar una tarea como completada (complete_task)
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')  # Redirigir a la lista de tareas

# Vista para eliminar una tarea (delete_task)
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')  # Redirigir a la lista de tareas

# Vista para cerrar sesión (signout)
def signout(request):
    logout(request)
    return redirect('home')

# Vista para iniciar sesión (signin)
def signin(request):
    if request.method == 'GET':
        # Si la solicitud HTTP es de tipo GET, renderizar el formulario de inicio de sesión
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        # Si la solicitud es de tipo POST (envío de formulario)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            # Si la autenticación es exitosa, iniciar sesión para el usuario y redirigirlo a la lista de tareas
            login(request, user)
            return redirect('tasks')

