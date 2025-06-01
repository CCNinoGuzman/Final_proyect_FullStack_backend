from django.shortcuts import render
from users.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .serializers import UserSerializer
from django.urls import path

@api_view (['GET'])
def list_users (request):
    list_user = User.objects.all () #select * from usuarios
    serializer = UserSerializer(list_user, many =True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view (['POST'])
def create_users(request):
    '''Crear usuario'''
    serializer = UserSerializer (data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_422_UNPROCESSABLE_ENTITY)
   

@api_view(['GET', 'PUT', 'DELETE'])
def detail_users(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'GET': 
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

