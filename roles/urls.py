from rest_framework.routers import DefaultRouter
from roles.views import rolesViewset

ulrpatterns=[
    path('task/', listtasks, name='lista_tareas' )
]