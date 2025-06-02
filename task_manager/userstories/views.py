from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Userstories
from .serializer import UserstoriesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def userstories_list(request):
    if request.method == 'GET':
        userstories = Userstories.objects.all()
        serializer = UserstoriesSerializer(userstories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserstoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)