from rest_framework import viewsets

from .serializers import ProfileSerializer, RuleSerializer
from ..models import Profile, Rule


class RuleViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``Rule``"""
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``Profile``"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
