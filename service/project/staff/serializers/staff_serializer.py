from rest_framework import serializers

from staff.models import StaffBase


class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = '__all__'
