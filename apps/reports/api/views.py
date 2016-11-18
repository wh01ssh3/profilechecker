from rest_framework import viewsets

from .serializers import OneTimeReportSerializer
from ..models import OneTimeReport


class OneTimeReportViewSet(viewsets.ModelViewSet):
    """ViewSet for ``OneTimeReport``"""

    queryset = OneTimeReport.objects.all()
    serializer_class = OneTimeReportSerializer
