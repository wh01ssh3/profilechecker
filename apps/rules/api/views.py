from rest_framework import viewsets

from apps.rules.api.serializers import RuleSerializer
from apps.rules.models import Rule


class RuleViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for ``Rule``"""

    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
