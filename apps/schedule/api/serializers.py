from rest_framework import serializers

from ..models import OneTimeTask, PeriodicTask
from ...rules.api.serializers import ProfileSerializer, RuleSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Base class for task serializers"""
    profiles = ProfileSerializer(many=True)
    rules = RuleSerializer(many=True)


class OneTimeTaskSerializer(TaskSerializer):
    """Serializer for ``OneTimeTask`` model"""

    class Meta:
        model = OneTimeTask
        fields = '__all__'


class PeriodicTaskSerializer(TaskSerializer):
    """Serializer for ``PeriodicTimeTask`` model"""

    class Meta:
        model = PeriodicTask
        fields = '__all__'
