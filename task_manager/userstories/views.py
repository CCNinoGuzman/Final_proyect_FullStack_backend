#from django.shortcuts import render
from .models import Userstories
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Userstories
from .serializer import UserstoriesSerializer
from django.shortcuts import get_list_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def userstories_list(request):
    if request.method == 'GET':
        Userstories = Userstories.objets.all()
        serializer = UserstoriesSerializer(Userstories)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserstoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
