from rest_framework import serializers
from Projectusers.models import Projectuser
from Users.models import Usuario

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectuser
        fields = ['id', 'name']  # Ajusta los campos según tu modelo Project

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name']  # Ajusta los campos según tu modelo Usuario

class ProjectuserSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    user = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Projectuser
        fields = ['id', 'project', 'user', 'rol']