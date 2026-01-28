# Arquitectura Software 1 - Registro de Usuarios

Proyecto Django con PostgreSQL para registro de usuarios.

## Requisitos

- Python 3.10+
- uv
- Docker

## Instalacion

```bash
# Clonar el repositorio
git clone https://github.com/Unbot2313/arquitectura_software_1
cd arquitectura_software_1

# Instalar dependencias
uv sync
```

## Ejecutar

```bash
# Levantar PostgreSQL
docker compose up -d

# Aplicar migraciones
uv run python manage.py migrate

# Iniciar servidor
uv run python manage.py runserver
```

## Rutas

- http://127.0.0.1:8000/ - Formulario de registro
- http://127.0.0.1:8000/usuarios/ - Lista de usuarios
