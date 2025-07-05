from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Project
from .models import Userstories

class UserstoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userstories
        fields = '__all__'
        #fields = ['id', 'title', 'project', 'state',  'story_items', 'estimated_time', 'user_id', 'scrum_id']

        
    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("El usuario (user_id) no existe.")
        return value

    def validate_scrum_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("El scrum master (scrum_id) no existe.")
        return value

    def validate_project(self, value):
        if not Project.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El proyecto no existe.")
        return value
