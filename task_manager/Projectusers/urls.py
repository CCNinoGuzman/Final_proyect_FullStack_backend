from django.urls import path
from .views import list_projectusers, create_projectuser, detail_projectuser

urlpatterns = [
    path('', list_projectusers, name='list_projectusers'),
    path('create', create_projectuser, name='create_projectuser'),
    path('<int:id>', detail_projectuser, name='detail_projectuser'),
]