from rest_framework import serializers

from apps.rules.api.serializers import ProfileSerializer
from ..models import OneTimeTask


class OneTimeTaskSerializer(serializers.ModelSerializer):
    """Serializer for ``OneTimeTask`` model"""

    profiles = ProfileSerializer(many=True)

    class Meta:
        model = OneTimeTask
        fields = '__all__'
