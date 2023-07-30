from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import response_ok, response_error, LResponse
from order.models import OrderDetail
from order.serializers.order_serializer import OrderDetailSerializer


class OrderDetailView(ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        """获取订单基础信息"""
        response = super().retrieve(request, *args, **kwargs)
        return LResponse(response.data).ok()

    @action(methods=["get"], detail=False, url_path="findByList", url_name="findByList")
    def find_by_list(self, request):
        """根据订单查询"""
        list_id = request.query_params.get("list_id")
        if not list_id and list_id != 0:
            return LResponse().error("订单id不能为空！")

        queryset = self.queryset.filter(order_list=list_id).order_by("-id")
        serializer = self.get_serializer(queryset, many=True)
        return LResponse(serializer.data).ok()

