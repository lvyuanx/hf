from rest_framework import serializers

from order.models import OrderList, OrderBase, OrderDetail, OrderType


class OrderBaseSerializer(serializers.ModelSerializer):
    order_type_name = serializers.CharField(source="order_type.name", read_only=True)
    model_base_name = serializers.CharField(source="model_base.name", read_only=True)

    # model_base_code = serializers.CharField(source="model_base.order_code", read_only=True)
    # model_base_product = serializers.CharField(source="model_base.order_product", read_only=True)

    class Meta:
        model = OrderBase
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'
