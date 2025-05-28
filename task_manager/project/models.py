from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
