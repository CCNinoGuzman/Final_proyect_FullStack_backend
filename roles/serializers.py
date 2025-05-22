from rest_framework import serializers 
from .models import roles

class RolesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = roles
        fields = '__all__' 

