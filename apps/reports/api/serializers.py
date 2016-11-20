from rest_framework import serializers

from ..models import OneTimeReport, PeriodicReport


class OneTimeReportSerializer(serializers.ModelSerializer):
    """Serializer for ``OneTimeReport``"""

    class Meta:
        model = OneTimeReport
        exclude = ('total_rules',)


class PeriodicReportSerializer(serializers.ModelSerializer):
    """Serializer for ``PeriodicReport``"""

    class Meta:
        model = PeriodicReport
        exclude = ('total_rules',)
