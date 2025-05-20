from django.shortcuts import render
from .models import Usuario

# Create your views here.
def lista_usuarios(request):
    usuarios = Usuario.objects.all() # select * from usuarios
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})