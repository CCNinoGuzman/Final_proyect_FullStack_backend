from django.db import models
from tasks.models import tasks
from Users.models import User 


class History(models.Model):
    task = models.ForeignKey(tasks, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    action = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    detail = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} - {self.action} on Tarea {self.task.id}"