from rest_framework.routers import DefaultRouter
from roles.views import rolesViewset

router=DefaultRouter()

router.register('', rolesViewset, basename='roles')
urlpatterns= router.urls