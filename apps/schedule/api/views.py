from rest_framework import viewsets

from .serializers import OneTimeTaskSerializer
from ..models import OneTimeTask


class OneTimeTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``OneTimeTask``"""
    queryset = OneTimeTask.objects.all()
    serializer_class = OneTimeTaskSerializer
