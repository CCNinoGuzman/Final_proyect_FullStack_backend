from rest_framework.routers import DefaultRouter
from tasks.views import TasksVieeSet

router=DefaultRouter()

router.register('tasks', TasksVieeSet, basename='tasks')
urlpatterns= router.urls