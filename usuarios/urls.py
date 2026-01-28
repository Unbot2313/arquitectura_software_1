from django.urls import path
from .views import crear_usuario, listar_usuarios

urlpatterns = [
    path('', crear_usuario, name='crear_usuario'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
]
