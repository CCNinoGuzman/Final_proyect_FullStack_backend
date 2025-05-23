from django.db import models

user_role = [
        (1, 'Esocoge el rol'),
        (2, 'Project Management Officer'),
        (3, 'Facilitador del equipo SCRUM'),
        (4, 'Encargado del desarrollo de software'),
    ]
# Create your models here.
class roles(models.Model):
    name_rol = models.CharField(max_length=100)
    description = models.TextField()
    roles = models.IntegerField(
        null=False, blank=False,
        choices=user_role,
        default=1
    )
    
    def __str__(self):
        return self.name_rol