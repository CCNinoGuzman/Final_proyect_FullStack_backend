from django.db import models

# Create your models here.
class Usuario (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) #Name VARCHAR(100) NOT NULL
    contraseña = models.CharField(max_length=50) #Password VARCHAR(50) NOT NULL
    correo = models.EmailField(max_length=100) #Email VARCHAR(100) NOT NULL   

    def __str__(self):
        return self.nombre
    