from django.db import models
#from Projectusers.models import Projectuser

# Create your models here.
class roles(models.Model):
    ROLE_CHOICES = [
        ('PMO', 'PMO'),
        ('Scrum Master', 'Scrum Master'),
        ('Desarrollador', 'Desarrollador'),
    ]
    name_rol =  models.CharField(max_length=50, choices=ROLE_CHOICES, null=True)
    description = models.TextField()

    
    def __str__(self):
        return self.name_rol