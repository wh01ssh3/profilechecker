from rest_framework.routers import DefaultRouter

from .views import OneTimeTaskViewSet

router = DefaultRouter()
router.register('one-time-tasks', OneTimeTaskViewSet)

urlpatterns = router.urls
