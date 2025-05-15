from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Invitation
from .serializers import InvitationSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def invitation_list(request):
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
def invitation_project(request, project_id):
    if request.method == 'GET':
        invitations = Invitation.objects.filter(project_id=project_id)
        serializer = InvitationSerializer(invitations, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def accept_invitation(request, pk):
    if request.method == 'PATCH':
        invitation = get_object_or_404(Invitation, pk=pk)
        serializer = InvitationSerializer(invitation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
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
def delete_invitation(request, pk):
    if request.method == 'DELETE':
        invitation = get_object_or_404(Invitation, pk=pk)
        invitation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)