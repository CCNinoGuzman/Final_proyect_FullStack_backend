from django.db import models

# Create your models here.
class Usuario (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) #Name VARCHAR(100) NOT NULL
    password = models.CharField(max_length=50) #Password VARCHAR(50) NOT NULL
    email = models.EmailField(max_length=100, unique=True) #Email VARCHAR(100) NOT NULL   

    def __str__(self):
        return self.name
    