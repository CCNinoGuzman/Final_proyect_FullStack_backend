from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import tasks 
from tasks.serializers import  TasksSerializer
from rest_framework import viewsets

# Create your views here.

class TasksVieeSet(viewsets.ModelViewSet):
    queryset = tasks.objects.all()
    serializer_class = TasksSerializer
    