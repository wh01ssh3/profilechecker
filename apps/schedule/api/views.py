from rest_framework import viewsets

from .serializers import OneTimeTaskSerializer, PeriodicTaskSerializer
from ..models import OneTimeTask, PeriodicTask


class OneTimeTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``OneTimeTask``"""

    def get_queryset(self):
        """User should be able to see only his tasks"""
        return OneTimeTask.objects.filter(user=self.request.user)

    serializer_class = OneTimeTaskSerializer


class PeriodicTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``PeriodicTask``"""

    def get_queryset(self):
        """User should be able to see only his tasks"""
        return PeriodicTask.objects.filter(user=self.request.user)

    serializer_class = PeriodicTaskSerializer
