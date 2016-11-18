from rest_framework import serializers

from ..models import Rule


class RuleSerializer(serializers.ModelSerializer):
    """Serializer for ``Rule``"""

    class Meta:
        model = Rule
        fields = '__all__'
