from django.db import models
from project.models import Project
from Users.models import User

# Create your models here.      
class Projectuser(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    ROLE_CHOICES = [
        ('PMO', 'PMO'),
        ('Scrum Master', 'Scrum Master'),
        ('Desarrollador', 'Desarrollador'),
    ]
    rol = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.name} - {self.project.name}"