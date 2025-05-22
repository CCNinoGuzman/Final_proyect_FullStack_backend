from rest_framework import serializers
from .models import tasks

class tasksSerializer(serializers.model_meta):
    
    class Meta:
        model= tasks
        fields= '__all__'