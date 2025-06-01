from django.db import models
from tasks.models import tasks
from Users.models import Usuario 


class History(models.Model):
    tarea = models.ForeignKey(tasks, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion} on Tarea {self.tarea.id}"