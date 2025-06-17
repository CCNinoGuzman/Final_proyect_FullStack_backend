from django.urls import path 
from  . import views

urlpatterns = [
    path('',views.roles_list, name='role'),
    path('create/', views.enter_roles, name='create_role'),
    path('<int:roles_id>', views.detail_role, name='see_refresh_erase'),
]