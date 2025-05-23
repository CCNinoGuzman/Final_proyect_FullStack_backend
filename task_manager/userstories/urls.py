from django.urls import path 
from  . import views
from userstories.views import userstories_list

urlpatterns = [
    path('userstories/', userstories_list, name='lista de historias de usuario')

]


