from django.db import models
from userstories.models import Userstories
from Users.models import User

# Creclass roles(models.Model):
class tasks(models.Model):
    user_history = models.ForeignKey(Userstories, on_delete=models.CASCADE, null=True, blank=True) 
    title=models.TextField
    developer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    description = models.CharField(max_length=150, null=True)
    state = models.CharField(max_length=100)
     
    def __str__(self):
        return self.user_history