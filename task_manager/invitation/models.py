from django.db import models
from project.models import Project  

class Invitation(models.Model):

    STATES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='invitations')
    state = models.CharField(max_length=10, choices=STATES, default='pending')
    token = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Invitation to {self.email} - State: {self.state}'