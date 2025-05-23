from django.db import models
from django.contrib.auth import get_user_model
from project.models import Project

User = get_user_model()

def get_first_user():
    return User.objects.first().id if User.objects.exists() else None


class Userstories(models.Model):
    STATES = [
        ('to_do', 'To Do'),
        ('progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='userstories')
    state = models.CharField(max_length=10, choices=STATES, default='to_do')
    story_items = models.CharField(max_length=100)
    estimated_time = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='userstories',
        default=get_first_user
    )
    scrum_master = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='scrum_stories',
        default=get_first_user
    )

    def __str__(self):
        return self.title
