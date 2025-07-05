import re
from rest_framework import serializers
from users.models import User

def validate_unique_name(value):
    if value and User.objects.filter(name__iexact=value).exists():
        raise serializers.ValidationError("Ya existe un usuario con el mismo nombre.")
    return value

def validate_unique_email(value):
    if value and User.objects.filter(email__iexact=value).exists():
        raise serializers.ValidationError("Ya existe una cuenta con este correo electrónico asociado.")
    return value

def validate_password(value):
    if value:
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>/]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos un carácter especial.")
        if not re.search(r'[a-zA-Z]', value) or not re.search(r'\d', value):
            raise serializers.ValidationError("La contraseña debe contener letras y números.")
    return value

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[validate_unique_name], required=False)
    email = serializers.EmailField(max_length=100, validators=[validate_unique_email], required=False)
    password = serializers.CharField(max_length=20, validators=[validate_password], write_only=True, required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'password', 'email']

    def create(self, validated_data):
        # Generar username si no se proporciona
        if not validated_data.get('username'):
            validated_data['username'] = validated_data['email'].split('@')[0]
        
        # Crear usuario usando solo los campos que el modelo acepta
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            # Asignar el campo name después de crear el usuario
            if 'name' in validated_data:
                user.name = validated_data['name']
                user.save()
            
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            raise serializers.ValidationError(f"Error al crear usuario: {str(e)}")

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance