from django.urls import path
from . import views

urlpatterns = [
    path('api/history/', views.history_list, name='history_list'),
    path('api/history/<int:pk>/', views.history_detail, name='history_detail'),
    path('api/history/task/<int:task_id>/', views.history_by_task, name='history_by_task'),
    path('api/history/user/<int:user_id>/', views.history_by_user, name='history_by_user')
]