from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from ..models import OneTimeTask, PeriodicTask
from ...rules.api.serializers import RuleSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Base class for task serializers"""
    rules = SerializerMethodField()

    def get_rules(self, obj):
        """Collect rules from profiles and rules of task"""
        rules = obj.get_all_rules()
        serializer = RuleSerializer(instance=rules, many=True)
        return serializer.data


class OneTimeTaskSerializer(TaskSerializer):
    """Serializer for ``OneTimeTask`` model"""

    class Meta:
        model = OneTimeTask
        exclude = ('user',)


class PeriodicTaskSerializer(TaskSerializer):
    """Serializer for ``PeriodicTimeTask`` model"""

    class Meta:
        model = PeriodicTask
        exclude = ('user',)
