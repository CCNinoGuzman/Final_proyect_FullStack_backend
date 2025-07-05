from django.shortcuts import render
from rest_framework.decorators  import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Invitation
from .serializers import InvitationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_invitation(request):
    if request.method == 'GET':
        invitations = Invitation.objects.all()
        serializer = InvitationSerializer(invitations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invitation_project(request, project_id):
    if request.method == 'GET':
        invitations = Invitation.objects.filter(project_id=project_id)
        serializer = InvitationSerializer(invitations, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def accept_invitation(request, pk):
    if request.method == 'PATCH':
        invitation = get_object_or_404(Invitation, pk=pk)
        serializer = InvitationSerializer(invitation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_invitation(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    serializer = InvitationSerializer(invitation, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def decline_invitation(request, pk):
    if request.method == 'PATCH':
        invitation = get_object_or_404(Invitation, pk=pk)
        serializer = InvitationSerializer(invitation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_invitation(request, pk):
    if request.method == 'DELETE':
        invitation = get_object_or_404(Invitation, pk=pk)
        invitation.delete()
        return Response({'mensaje': 'Invitación eliminada'}, status=204)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def invitation_detail(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    
    if request.method == 'GET':
        serializer = InvitationSerializer(invitation)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = InvitationSerializer(invitation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        invitation.delete()
        return Response({'mensaje': 'Invitación eliminada'}, status=status.HTTP_204_NO_CONTENT)

