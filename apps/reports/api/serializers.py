from rest_framework import serializers

from ..models import OneTimeReport, PeriodicReport


class ReportSerializer(serializers.ModelSerializer):
    """Base report serializer class"""

    def __init__(self, *args, **kwargs):
        """Filter queryset of task by user"""
        request = kwargs.get('context').get('request')
        task = self.fields['task']
        task.queryset = task.queryset.filter(user=request.user)
        super().__init__(*args, **kwargs)


class OneTimeReportSerializer(ReportSerializer):
    """Serializer for ``OneTimeReport``"""

    class Meta:
        model = OneTimeReport
        exclude = ('total_rules',)


class PeriodicReportSerializer(ReportSerializer):
    """Serializer for ``PeriodicReport``"""

    class Meta:
        model = PeriodicReport
        exclude = ('total_rules',)
