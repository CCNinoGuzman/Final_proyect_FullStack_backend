from django.db import models

from task_manager.project.models import Project

# Create your models here.
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
    user_id = models.IntegerField()
    scrum_id = models.IntegerField()

    def __str__(self):
        return self.title
