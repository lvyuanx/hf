from rest_framework import serializers

from order.models import StepBase, StepSort


class StepBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepBase
        fields = '__all__'


class StepSortSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepSort
        fields = '__all__'
