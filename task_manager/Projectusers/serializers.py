from rest_framework import serializers
from projectusers.models import Projectuser
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectuser
        fields = ['id', 'name']  # Ajusta los campos según tu modelo Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']  # Ajusta los campos según tu modelo Usuario

class ProjectuserSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Projectuser
        fields = ['id', 'project', 'user', 'rol']