from django.urls import path
from .views import userstories_list, userstories_detail, whoami

urlpatterns = [
    path('', userstories_list, name='userstories_list'),
    path('<int:pk>/', userstories_detail, name='userstories_detail'),
    path('whoami/', whoami, name='whoami')
]