from rest_framework import serializers
from Users.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['name', 'password', 'email']

        

