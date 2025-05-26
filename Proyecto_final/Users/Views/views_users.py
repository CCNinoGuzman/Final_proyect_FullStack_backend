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





   