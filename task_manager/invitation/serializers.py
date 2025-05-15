from rest_framework import serializers  
from .models import invitation

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = invitation
        fields = ['id', 'email', 'project_id', 'state', 'token']