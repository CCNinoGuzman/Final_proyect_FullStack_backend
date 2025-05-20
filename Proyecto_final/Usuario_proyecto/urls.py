from django.urls import path
from .migrations import views

urlpatterns = [
    path('', views.proyecto_usuarios, name='proyecto_usuarios'),
]