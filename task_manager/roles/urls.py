from rest_framework.routers import DefaultRouter
from roles.views import rolesViewset

router=DefaultRouter()

router.register('roles', rolesViewset, basename='roles')
urlpatterns= router.urls