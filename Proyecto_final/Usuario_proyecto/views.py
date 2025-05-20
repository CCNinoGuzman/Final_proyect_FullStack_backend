from django.shortcuts import render
from .models import UsuarioProyecto

def proyecto_usuarios(request):
    usuarios_proyecto = UsuarioProyecto.objects.all()
    return render(request, 'usuarios/proyecto_usuarios.html', {'usuarios_proyecto': usuarios_proyecto})

