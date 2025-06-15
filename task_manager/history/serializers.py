from rest_framework import serializers  
from .models import History
from django.contrib.auth import get_user_model
User = get_user_model()

class HistorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = History
        fields = '__all__'