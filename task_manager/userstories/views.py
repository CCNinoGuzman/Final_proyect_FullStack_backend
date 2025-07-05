from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserstoriesSerializer
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response


logger = logging.getLogger(__name__)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def userstories_detail(request, pk):
    """
    Recupera, actualiza o elimina una historia de usuario por su ID.
    Solo el usuario creador o el scrum master pueden modificar o eliminar.
    """
    try:
        historia = Userstories.objects.get(pk=pk)
    except Userstories.DoesNotExist:
        logger.warning(f"Intento de acceso a historia inexistente: {pk}")
        return Response({'error': 'Historia no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error inesperado al acceder a historia {pk}: {str(e)}")
        return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        serializer = UserstoriesSerializer(historia)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # if request.user != historia.user and request.user != historia.scrum_master:
        #     logger.warning(f"Usuario {request.user} intentó editar historia {pk} sin permiso")
        #     return Response({'error': 'No tienes permiso para editar esta historiaa'},
        #                     status=status.HTTP_403_FORBIDDEN)

        serializer = UserstoriesSerializer(historia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Historia {pk} actualizada por {request.user}")
            return Response(serializer.data)
        logger.warning(f"Datos inválidos al actualizar historia {pk}: {serializer.errors}")
        return Response({'error': 'Datos inválidos', 'detalles': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # if request.user != historia.user and request.user != historia.scrum_master:
        #     logger.warning(f"Usuario {request.user} intentó eliminar historia {pk} sin permiso")
        #     return Response({'error': 'No tienes permiso para eliminar esta historia'},
        #                     status=status.HTTP_403_FORBIDDEN)

        historia.delete()
        logger.info(f"Historia {pk} eliminada por {request.user}")
        return Response({'mensaje': 'Historia eliminada'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def userstories_list(request):
    """
    Lista todas las historias de usuario o crea una nueva.
    """
    if request.method == 'GET':
        historias = Userstories.objects.all()
        serializer = UserstoriesSerializer(historias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserstoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def whoami(request):
    return Response({'user_id': request.user.id, 'username': str(request.user)})

@api_view(['POST'])
def userstories_create(request):
    serializer = UserstoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)