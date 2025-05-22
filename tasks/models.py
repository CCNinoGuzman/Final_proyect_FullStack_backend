from django.db import models

# Creclass roles(models.Model):
class tasks(models.Model):
    historial_usuario_id = models.PositiveIntegerField()
    descripcion = models.TextField(null=True)
    estado = models.CharField(max_length=100)
    
    def __str__(self):
        return self.historial_usuario_id