from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_invitation, name='list_invitation'),
    path('<int:pk>/', views.detail_invitation, name='detail_invitation'),
    path('<int:project_id>/', views.invitation_project, name='invitation_project'),
    path('<int:pk>/accept/', views.accept_invitation, name='accept_invitation'),
    path('<int:pk>/reject/', views.decline_invitation, name='decline_invitation'),
    path('<int:pk>/delete/', views.delete_invitation, name='delete_invitation'),
]