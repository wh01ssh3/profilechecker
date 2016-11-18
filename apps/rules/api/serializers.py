from rest_framework import serializers

from ..models import Profile, Rule


class RuleSerializer(serializers.ModelSerializer):
    """Serializer for ``Rule``"""

    class Meta:
        model = Rule
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for ``Profile``"""

    rules = RuleSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'
