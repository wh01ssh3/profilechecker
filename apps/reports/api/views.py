from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .serializers import OneTimeReportSerializer
from ..models import OneTimeReport
from ...schedule.models import OneTimeTask


class OneTimeReportViewSet(viewsets.ModelViewSet):
    """ViewSet for ``OneTimeReport``"""

    def get_queryset(self):
        return OneTimeReport.objects.filter(task__user=self.request.user)

    def perform_create(self, serializer):
        task = OneTimeTask.objects.get(id=serializer.data['task'])
        if task.user != self.request.user:
            raise ValidationError(
                _('You can\'t create reports of not your tasks'))

    serializer_class = OneTimeReportSerializer
