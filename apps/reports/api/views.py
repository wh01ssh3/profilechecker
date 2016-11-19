from django.utils.translation import ugettext_lazy as _
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import GenericViewSet

from apps.schedule.models import PeriodicTask
from .serializers import OneTimeReportSerializer, PeriodicReportSerializer
from ..models import OneTimeReport, PeriodicReport
from ...schedule.models import OneTimeTask


class OneTimeReportViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           # Disallow to remove and update
                           GenericViewSet):
    """ViewSet for ``OneTimeReport``"""

    def get_queryset(self):
        """User should see only his reports"""
        return OneTimeReport.objects.filter(task__user=self.request.user)

    def perform_create(self, serializer):
        """Create report

        User shouldn't be able to create report for task, which is not his
        task. Also user shouldn't be able to create the second report for task,
        which already has report
        """
        task = OneTimeTask.objects.get(id=serializer.data['task'])
        if task.user != self.request.user:
            raise ValidationError(
                _('You can\'t create reports of not your tasks'))
        if task.reports.all().exists():
            raise ValidationError(_('This task already have report'))

    serializer_class = OneTimeReportSerializer


class PeriodicReportViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            # Disallow to remove and update
                            GenericViewSet):
    """ViewSet for ``PeriodicReport``"""

    def get_queryset(self):
        """User should see only his reports"""
        return PeriodicReport.objects.filter(task__user=self.request.user)

    def perform_create(self, serializer):
        """Create report"""
        task = PeriodicTask.objects.get(id=serializer.data['task'])
        if task.user != self.request.user:
            raise ValidationError(
                _('You can\'t create reports of not your tasks'))

    serializer_class = PeriodicReportSerializer
