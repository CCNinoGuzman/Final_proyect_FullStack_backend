from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Projectuser
from .serializers import ProjectuserSerializer


@api_view(['GET'])
def list_projectusers(request):
    projectusers = Projectuser.objects.all()
    serializer = ProjectuserSerializer(projectusers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_projectuser(request):
    serializer = ProjectuserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_projectuser(request, pk):
    projectuser = get_object_or_404(Projectuser, pk=pk)

    if request.method == 'GET':
        serializer = ProjectuserSerializer(projectuser)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProjectuserSerializer(projectuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    elif request.method == 'DELETE':
        projectuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)