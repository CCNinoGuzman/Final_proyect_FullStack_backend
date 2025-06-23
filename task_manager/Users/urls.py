from django.urls import path
from .views import detail_users, list_users, create_users, login_user

urlpatterns = [
    path('', list_users, name='list_users'),
    path('create/', create_users, name= 'create_users'),
    path('<int:user_id>', detail_users, name='detail_user'),
    path('login/', login_user, name='login_user')
    
]