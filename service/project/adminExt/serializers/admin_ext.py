from rest_framework import serializers

from adminExt.models import SPremission


class SPremissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPremission
        fields = '__all__'