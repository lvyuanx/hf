from rest_framework import serializers

from manager.models import SPremission, SRole


class SPremissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPremission
        fields = '__all__'


class SRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRole
        fields = '__all__'


class SRoleLiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRole
        fields = ('id', 'notes')
