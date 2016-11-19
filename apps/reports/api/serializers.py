from rest_framework import serializers

from apps.reports.models import PeriodicReport
from ..models import OneTimeReport


class OneTimeReportSerializer(serializers.ModelSerializer):
    """Serializer for ``OneTimeReport``"""

    class Meta:
        model = OneTimeReport
        fields = '__all__'


class PeriodicReportSerializer(serializers.ModelSerializer):
    """Serializer for ``PeriodicReport``"""

    class Meta:
        model = PeriodicReport
        fields = '__all__'
