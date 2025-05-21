from django.db import models
from Task.models import Task 
from User.models import User 


class History(models.Model):
    tarea = models.ForeignKey(Task, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion} on Tarea {self.tarea.id}"