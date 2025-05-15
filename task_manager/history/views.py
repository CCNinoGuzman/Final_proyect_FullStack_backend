from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import History
from .serializers import HistorySerializer  
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def history_by_task(request, task_id):
        history = History.objects.filter(task_id=task_id)
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def history_by_user(request, user_id):
        history = History.objects.filter(user_id=user_id)
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def history_list(request):
    if request.method == 'GET':
        histories = History.objects.all()
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE']) 
def history_detail(request, pk):
    history = get_object_or_404(History, pk=pk)
    if request.method == 'GET':
        serializer = HistorySerializer(history)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif request.method == 'DELETE':
        history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)