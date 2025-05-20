from django.db import models
from .models import Proyecto, Rol, Usuario

# Create your models here.
class Usuario_proyecto(models.Model):
 proyecto_id = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)
usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

def __str__(self):
        return f"{self.usuario.nombre} - {self.proyecto.nombre} - {self.rol.nombre}"