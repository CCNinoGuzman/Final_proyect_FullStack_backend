from django.db import models
class History(models.Model):
# Create your models here.
    task_id = models.IntegerField()
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History {self.id} for Task {self.task_id}"

