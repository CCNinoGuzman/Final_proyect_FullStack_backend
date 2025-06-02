from django.db import models

# Creclass roles(models.Model):
class tasks(models.Model):
    history_user_id = models.PositiveIntegerField()
    description = models.TextField(null=True)
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.history_user_id 