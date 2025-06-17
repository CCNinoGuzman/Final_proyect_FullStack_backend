from rest_framework import serializers
from .models import tasks

class TasksSerializer(serializers.ModelSerializer):
        
    class Meta:
        model= tasks
        fields=['user_history', 'title', 'developer',  'description', 'state' ]