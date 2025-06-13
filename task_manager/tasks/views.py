from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  tasks
from .serializers import TasksSerializer

# Create your views here.

@api_view (['GET'])
def tasks_list(request):
    '''Listrar tareas'''
    task = tasks.objects.all()
    serializer = TasksSerializer(task, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
    

@api_view (['POST'])
def enter_task(request):
    '''Crear tareas'''
    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

    
@api_view(['GET', 'PUT', 'DELETE'])
def detail_task(request, tasks_id):
    '''obtener actualizar o eliminar'''
    task = get_object_or_404(tasks, id=tasks_id)
    
    if request.method == "GET":
        serializer = TasksSerializer(task)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = TasksSerializer(task, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

    if request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        