from rest_framework.routers import DefaultRouter

from .views import OneTimeTaskViewSet, PeriodicTaskViewSet

router = DefaultRouter()
router.register('one-time-tasks', OneTimeTaskViewSet,
                base_name='one_time_tasks')
router.register('periodic-tasks', PeriodicTaskViewSet,
                base_name='periodic_tasks')

urlpatterns = router.urls
