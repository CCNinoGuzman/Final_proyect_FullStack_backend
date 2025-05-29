from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_project, name='api_project_list'),
    path('<int:pk>/', views.detail_project, name='api_project_detail'),
]