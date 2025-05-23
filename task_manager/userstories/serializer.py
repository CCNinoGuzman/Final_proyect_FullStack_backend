from .models import Userstories
from rest_framework import serializers


class UserstoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userstories
        fields = ['id', 'title', 'project', 'state',  'story_items', 'estimated_time', 'user_id', 'scrum_id']

        
    