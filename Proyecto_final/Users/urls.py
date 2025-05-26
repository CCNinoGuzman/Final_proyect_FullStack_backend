from django.urls import path
from Users.Views.views_users import list_users

urlpatterns = [
    path('Users/', list_users, name='lista_usuarios'),
]