from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import tasks
from .serializer import tasksSerializer



# Create your views here.
def list_task(request):
    '''lisstar tasks'''
    products = tasks.object()
    