from rest_framework import serializers  
from .models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'task_id', 'user_id', 'action', 'date', 'detail', 'module']