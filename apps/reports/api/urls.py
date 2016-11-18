from rest_framework.routers import DefaultRouter

from .views import OneTimeReportViewSet

router = DefaultRouter()
router.register('one-time-reposts', OneTimeReportViewSet)

urlpatterns = router.urls
