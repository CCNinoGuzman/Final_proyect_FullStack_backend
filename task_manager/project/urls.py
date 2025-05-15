from django.urls import path
from . import views

urlpatterns = [
    path('api/projects/', views.project_list, name='api_project_list'),
    path('api/projects/<int:pk>/', views.detail_project, name='api_project_detail'),
]