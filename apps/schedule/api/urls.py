from rest_framework.routers import DefaultRouter

from .views import OneTimeTaskViewSet

router = DefaultRouter()
router.register('one-time-tasks', OneTimeTaskViewSet,
                base_name='one-time-tasks')

urlpatterns = router.urls
