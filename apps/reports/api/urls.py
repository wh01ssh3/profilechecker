from rest_framework.routers import DefaultRouter

from .views import OneTimeReportViewSet, PeriodicReportViewSet

router = DefaultRouter()
router.register('one-time-reports', OneTimeReportViewSet,
                base_name='one_time_reports')
router.register('periodic-reports', PeriodicReportViewSet,
                base_name='one_time_reports')

urlpatterns = router.urls
