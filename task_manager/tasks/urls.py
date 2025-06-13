from django.urls import path 
from  . import views

urlpatterns = [
    path('',views.tasks_list, name='tasks'),
    path('create/', views.enter_task, name='create_tasks'),
    path('<int:tasks_id>', views.detail_task, name='create_tasks'),
]