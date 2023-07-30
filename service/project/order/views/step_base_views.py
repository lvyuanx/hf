from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import LResponse
from order.models import StepBase
from order.serializers.step_serializer import StepBaseSerializer


class StepBaseView(ModelViewSet):
    queryset = StepBase.objects.all()
    serializer_class = StepBaseSerializer

    def list(self, request, *args, **kwargs):
        """获取所有订单类型"""
        response = super().list(request, *args, **kwargs)
        return LResponse(response.data).ok()
