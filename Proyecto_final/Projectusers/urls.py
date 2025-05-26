from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projectusers, name='proyecto_usuarios'),
]