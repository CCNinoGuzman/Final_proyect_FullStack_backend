from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import roles 
from .serializers import RolesSerializer
from rest_framework import viewsets

# Create your views here.

class rolesViewset(viewsets.ModelViewSet):
    queryset = roles.objects.all()
    serializer_class = RolesSerializer
    
    
    