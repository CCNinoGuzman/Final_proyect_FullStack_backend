from django.urls import path
from .views import list_projectusers, create_projectuser, detail_projectuser

urlpatterns = [
    path('projectusers/', list_projectusers, name='list_projectusers'),
    path('projectusers/create/', create_projectuser, name='create_projectuser'),
    path('projectusers/<int:pk>/', detail_projectuser, name='detail_projectuser'),
]