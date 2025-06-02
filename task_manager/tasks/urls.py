from rest_framework.routers import DefaultRouter
from tasks.views import TasksVieeSet

router=DefaultRouter()

router.register(r'', TasksVieeSet, basename='tasks')
urlpatterns= router.urls