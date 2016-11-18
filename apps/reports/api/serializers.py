from rest_framework import serializers

from ..models import OneTimeReport


class OneTimeReportSerializer(serializers.ModelSerializer):
    """Serializer for ``OneTimeReport``"""

    class Meta:
        model = OneTimeReport
        fields = '__all__'
