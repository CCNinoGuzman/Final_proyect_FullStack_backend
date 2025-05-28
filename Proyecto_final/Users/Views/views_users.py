from django.shortcuts import render
from Users.models import Usuario
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Users.models import Usuario
from Users.Serializers.users_serializers import UsuarioSerializer
from django.urls import path

@api_view (['GET'])
def list_users (request):
    list_user = Usuario.objects.all () #select * from usuarios
    serializer = UsuarioSerializer(list_user, many =True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view (['POST'])
def create_users(request):
    '''Crear usuario'''
    serializer = UsuarioSerializer (data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_422_UNPROCESSABLE_ENTITY)
   

@api_view(['GET', 'PUT', 'DELETE'])
def detail_users(request, user_id):
    usuario = get_object_or_404(Usuario, user_id=user_id)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

