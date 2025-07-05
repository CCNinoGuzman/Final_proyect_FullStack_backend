from django.urls import path
from .views import list_project, detail_project, projects_by_user

urlpatterns = [
    path('', list_project, name='api_project_list'),
    path('<int:id>/', detail_project, name='api_project_detail'),
    path('user/<int:user_id>/', projects_by_user, name='projects_by_user'),
]