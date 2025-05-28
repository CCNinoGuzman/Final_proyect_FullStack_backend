from django.db import models

# Create your models here.
class Usuario (models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) #Name VARCHAR(100) NOT NULL
    password = models.CharField(max_length=20) #Password VARCHAR(20) NOT NULL
    email = models.EmailField(max_length=100, unique=True) #Email VARCHAR(100) NOT NULL   

    def __str__(self):
        return self.name
    