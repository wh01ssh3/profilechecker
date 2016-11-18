from rest_framework import viewsets

from .serializers import OneTimeTaskSerializer
from ..models import OneTimeTask


class OneTimeTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``OneTimeTask``"""

    def get_queryset(self):
        """User should be able to see only his tasks"""
        return OneTimeTask.objects.filter(user=self.request.user)

    serializer_class = OneTimeTaskSerializer
