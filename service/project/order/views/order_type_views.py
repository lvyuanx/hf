from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import LResponse
from order.models import OrderType
from order.serializers.OrderSerializer import OrderTypeSerializer


class OrderTypeView(ModelViewSet):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer

    def list(self, *args, **kwargs):
        """获取所有订单类型"""
        response = super().list(*args, **kwargs)
        return LResponse(response.data).ok()
