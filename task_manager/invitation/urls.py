from django.urls import path
from . import views

urlpatterns = [
    path('api/invitations/', views.invitation_list, name='api_invitation_list'),
    path('api/invitations/<int:pk>/', views.detail_invitation, name='api_invitation_detail'),
    path('api/invitations/projects/<int:project_id>/', views.invitation_project, name='api_invitation_project'),
    path('api/invitations/<int:pk>/accept/', views.accept_invitation, name='accept_invitation'),
    path('api/invitations/<int:pk>/reject/', views.reject_invitation, name='reject_invitation'),
    path('api/invitations/<int:pk>/delete/', views.delete_invitation, name='delete_invitation'),
]