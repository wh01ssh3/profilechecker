from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, RuleViewSet

router = DefaultRouter()
router.register('rules', RuleViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = router.urls
