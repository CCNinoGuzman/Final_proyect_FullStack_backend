from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_history, name='history_list'),
    path('detail/<int:pk>/', views.detail_history, name='history_detail'),
    path('task/<int:task_id>/', views.history_by_task, name='history_by_task'),
    path('user/<int:user_id>/', views.history_by_user, name='history_by_user')
]