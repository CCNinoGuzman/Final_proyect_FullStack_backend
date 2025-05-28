from django.urls import path
from Users.Views.views_users import detail_users, list_users, create_users

urlpatterns = [
    path('Users/', list_users, name='list_usuarios'),
    path('Users/create/', create_users, name= 'create_user'),
    path('Users/<int:user_id>', detail_users, name='detail_user')
    
]