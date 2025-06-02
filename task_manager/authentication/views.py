from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    View to handle user login and return JWT tokens.
    """

    #Obtenemos el usuario y contraseña que han sido enviados
    email_from_client = request.data.get('email')
    password_from_client = request.data.get('password')

    #Validamos que el usuario exista en la bd
    user = authenticate(request, username = email_from_client, password = password_from_client)

    #Generamos el token su el usuario existe en la bd
    if user and user.is_active:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
        },
        status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'error': 'Invalid credentials'
             }, 
             status.HTTP_401_UNAUTHORIZED
        )