from rest_framework.routers import DefaultRouter

from apps.rules.api.views import RuleViewSet

router = DefaultRouter()
router.register('rules', RuleViewSet)

urlpatterns = router.urls
