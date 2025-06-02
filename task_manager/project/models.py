from django.db import models
from users.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    STATES = [
        ('active','Active'),
        ('in_progress','In progress'),
        ('closed','Closed')
    ]
    state = models.CharField(max_length=20, choices=STATES, default='active')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name    
