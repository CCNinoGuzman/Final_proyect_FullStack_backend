from rest_framework import serializers
from Projectusers.models import Projectuser
from project.models import Project
from Users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class ProjectuserSerializer(serializers.ModelSerializer):

    project_detail = ProjectSerializer(source='project', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Projectuser
        fields = ['id', 'project', 'user', 'rol', 'project_detail', 'user_detail']
