import re
from rest_framework import serializers
from users.models import User

def validate_unique_name(value):
    if User.objects.filter(name__iexact=value).exists():
        raise serializers.ValidationError("Ya existe un usuario con el mismo nombre.")
    return value

def validate_unique_email(value):
    if User.objects.filter(email__iexact=value).exists():
        raise serializers.ValidationError("Ya existe una cuenta con este correo electrónico asociado.")
    return value

def validate_password(value):
    if not re.search(r'[A-Z]', value):
        raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>/]', value):
        raise serializers.ValidationError("La contraseña debe contener al menos un carácter especial.")
    if not re.search(r'[a-zA-Z]', value) or not re.search(r'\d', value):
        raise serializers.ValidationError("La contraseña debe contener letras y números.")
    return value

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[validate_unique_name])
    email = serializers.EmailField(max_length=100, validators=[validate_unique_email])
    password = serializers.CharField(max_length=20, validators=[validate_password], write_only=True)
    username = serializers.CharField(required=False)  # Para que puedas autogenerarlo

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'password', 'email']

    def create(self, validated_data):
        if not validated_data.get('username'):
            validated_data['username'] = validated_data['email'].split('@')[0]
        user = User.objects.create_user(**validated_data)
        return user