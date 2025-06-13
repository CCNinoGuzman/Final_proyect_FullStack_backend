from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  roles
from .serializers import RolesSerializer

# Create your views here.

@api_view (['GET'])
def roles_list(request):
    '''Listar roles'''
    task = roles.objects.all()
    serializer = RolesSerializer(task, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
    

@api_view (['POST'])
def enter_roles(request):
    '''Crear tareas'''
    serializer = RolesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@api_view(['GET', 'PUT', 'DELETE'])
def detail_role(request, roles_id):
    '''obtener actualizar o eliminar'''
    rol = get_object_or_404(roles, id=roles_id)
    
    if request.method == "GET":
        serializer = RolesSerializer(rol)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = RolesSerializer(rol, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

    if request.method == "DELETE":
        rol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        