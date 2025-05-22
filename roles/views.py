from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import status 
from .serializers import RolesSerializer

# Create your views here.

class rolesViewset(viewsets.ModelViewSet):
    queryset = roles.objects.all()
    serializer_class = RolesSerializer
    
    
    