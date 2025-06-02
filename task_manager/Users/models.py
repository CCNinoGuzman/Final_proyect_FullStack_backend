from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User (AbstractUser):
    name = models.CharField(max_length=100) #Name VARCHAR(100) NOT NULL
    email = models.EmailField(
        unique=True, 
        verbose_name='Dirección de correo electrónico'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None  # Disable the username field


    def __str__(self):
        return self.name
    