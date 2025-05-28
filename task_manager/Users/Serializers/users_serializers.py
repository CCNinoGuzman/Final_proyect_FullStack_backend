import re
from rest_framework import serializers
from Users.models import Usuario

def validate_unique_name (value):
    if Usuario.objects.filter(name__iexact = value).exists():
        raise serializers.ValidationError ("Ya existe un usuario con el mismo nombre.")
    else:
        return value
    
def validate_unique_email (value):
    if Usuario.objects.filter(email__iexact = value).exists():
        raise serializers.ValidationError ("Ya existe una cuenta con este correo electronico asociado.")
    else:
        return value
    
def validate_password(value):
    # Al menos una mayúscula
    if not re.search(r'[A-Z]', value):
        raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
    
    # Al menos un carácter especial (puedes ajustar los caracteres que consideres especiales)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>/]', value):
        raise serializers.ValidationError("La contraseña debe contener al menos un carácter especial.")
    
    # Debe ser alfanumérica (contener letras y números)
    # Aquí verificamos que tenga al menos una letra y un número
    if not re.search(r'[a-zA-Z]', value) or not re.search(r'\d', value):
        raise serializers.ValidationError("La contraseña debe contener letras y números.")

    return value

class UsuarioSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length = 100, validators = [validate_unique_name])
    email = serializers.EmailField(max_length =100, validators = [validate_unique_email])
    password = serializers.CharField(max_length=20, validators=[validate_password])
    

    class Meta:
        model = Usuario
        fields = ['user_id', 'name', 'password', 'email']

        

