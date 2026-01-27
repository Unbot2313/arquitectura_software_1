#  Tarea: Registro de Usuario con Django y PostgreSQL

> **Lenguaje base:** Python 

##  Objetivo
El objetivo de esta tarea es que el estudiante aprenda a:
- Instalar y configurar **Django**
- Conectar un proyecto Django a una base de datos **PostgreSQL**
- Crear una interfaz web sencilla que solicite un **nombre de usuario**
- Guardar ese nombre de usuario en la base de datosa

---

##  ¿Por qué Python para esta tarea?

Python es un lenguaje de programación de alto nivel, muy utilizado en desarrollo web, ciencia de datos, automatización y backend. En esta tarea, Python es el lenguaje principal porque:

- Django está escrito completamente en Python
- Permite escribir código claro, legible y mantenible
- Tiene un ecosistema enorme de librerías (como `psycopg2` para PostgreSQL)
- Es uno de los lenguajes más usados profesionalmente en backend

Durante esta tarea usarás Python para:
- Definir modelos de base de datos
- Crear vistas (lógica del servidor)
- Manejar formularios HTML
- Conectarte a PostgreSQL

---

##  Requisitos previos
Antes de comenzar, asegúrate de tener instalado:
- Python 3.10 o superior
- pip
- PostgreSQL
- Git (opcional, pero recomendado)

---

##  Paso 1: Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

---

##  Paso 2: Instalar Django y dependencias

```bash
pip install django psycopg2-binary
```

---

##  Paso 3: Crear el proyecto y la aplicación

```bash
django-admin startproject usuario_project
cd usuario_project
python manage.py startapp usuarios
```

Agrega la app `usuarios` en `settings.py`:

```python
INSTALLED_APPS = [
    'usuarios',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

##  Paso 4: Configurar PostgreSQL

Crea una base de datos en PostgreSQL:

```sql
CREATE DATABASE usuarios_db;
CREATE USER usuario_django WITH PASSWORD 'password123';
ALTER ROLE usuario_django SET client_encoding TO 'utf8';
ALTER ROLE usuario_django SET default_transaction_isolation TO 'read committed';
ALTER ROLE usuario_django SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE usuarios_db TO usuario_django;
```

Configura la base de datos en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'usuarios_db',
        'USER': 'usuario_django',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

##  Paso 5: Crear el modelo

En `usuarios/models.py`:

```python
from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario
```

Aplica las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

##  Paso 6: Crear la vista y el formulario

En `usuarios/views.py`:

```python
from django.shortcuts import render, redirect
from .models import Usuario


def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_usuario')
        Usuario.objects.create(nombre_usuario=nombre)
        return redirect('crear_usuario')

    return render(request, 'usuarios/formulario.html')
```

---

##  Paso 7: Configurar URLs

En `usuarios/urls.py`:

```python
from django.urls import path
from .views import crear_usuario

urlpatterns = [
    path('', crear_usuario, name='crear_usuario'),
]
```

En `usuario_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
]
```

---

##  Paso 8: Crear la plantilla HTML

Crea la carpeta `templates/usuarios/` y el archivo `formulario.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro de Usuario</title>
</head>
<body>
    <h1>Registro de Usuario</h1>
    <form method="POST">
        {% csrf_token %}
        <input type="text" name="nombre_usuario" placeholder="Nombre de usuario" required>
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
```

---

##  Paso 9: Ejecutar el servidor

```bash
python manage.py runserver
```

Abre el navegador en: http://127.0.0.1:8000/

---

##  Subida del proyecto a GitHub

En esta sección aprenderás a usar **Git**, una herramienta de control de versiones, para subir tu proyecto a **GitHub**.

Git permite:
- Guardar el historial de cambios del proyecto
- Trabajar de forma profesional
- Compartir tu código y evidencias

###  Pasos detallados

1. Crea un repositorio nuevo en GitHub (público o privado según se indique).
2. Abre una terminal dentro de la carpeta raíz del proyecto Django.
3. Ejecuta los siguientes comandos uno por uno:

```bash
git init                # Inicializa un repositorio Git
git add .               # Agrega todos los archivos al control de versiones
git commit -m "Proyecto Django: registro de usuario"  # Guarda un primer commit
git branch -M main      # Renombra la rama principal
git remote add origin https://github.com/USUARIO/REPOSITORIO.git  # Conecta con GitHub
git push -u origin main # Sube el proyecto al repositorio remoto
```

4. Verifica en GitHub que los archivos aparezcan correctamente.

 **Importante:**
- Estos comandos **pueden fallar** dependiendo del sistema operativo, configuración local, versión de Git, permisos o credenciales.
- Es **responsabilidad del estudiante** investigar, diagnosticar y resolver los errores que aparezcan (troubleshooting).
- Parte fundamental de esta tarea es aprender a **leer mensajes de error**, buscar soluciones y aplicar correcciones.

No se aceptarán entregas incompletas debido a errores locales no resueltos.

3. Asegúrate de incluir un archivo `.gitignore` (puedes usar el de Python/Django).

1. Crea un repositorio nuevo en GitHub (público o privado según se indique).
2. Desde la carpeta raíz del proyecto:

```bash
git init
git add .
git commit -m "Proyecto Django: registro de usuario"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

3. Asegúrate de incluir un archivo `.gitignore` (puedes usar el de Python/Django).

---

##  Evidencia con imágenes

En el repositorio de GitHub debes incluir una carpeta llamada `screenshots/` con:

-  Imagen del formulario funcionando en el navegador
-  Imagen de la base de datos (por ejemplo, usando `psql`, pgAdmin o una consulta SQL mostrando el registro guardado)

Ejemplo de estructura:

```
/screenshots
 ├── formulario.png
 └── base_datos.png
```

Las imágenes deben estar correctamente visibles desde el README del repositorio.

---

##  Entregables

- Enlace al repositorio de GitHub
- Proyecto Django funcional
- Carpeta `screenshots/` con evidencias
- README explicando cómo ejecutar el proyecto

- Repositorio o carpeta del proyecto Django
- Captura de pantalla del formulario funcionando
- Evidencia (screenshot o consulta SQL) de que el usuario se guardó en PostgreSQL

---

##  Extra (opcional)
- Validar que el nombre de usuario no esté vacío
- Mostrar una lista de usuarios guardados
- Agregar estilos con CSS

Éxitos y buen código. 


