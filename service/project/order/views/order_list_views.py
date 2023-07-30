from django.db import transaction
from rest_framework.decorators import action
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import response_error, response_ok, LResponse
from order.models import OrderList
from order.serializers.order_serializer import OrderListSerializer, OrderDetailSerializer


class OrderListView(ModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer

    def retrieve(self, request,  *args, **kwargs):
        """获取订单基础信息"""
        response = super().retrieve(request, *args, **kwargs)
        return LResponse(response.data).ok()

    @action(methods=["post"], detail=False, url_path="edit", url_name="edit")
    @transaction.atomic
    def edit_order_list(self, request):
        """编辑订单列表"""
        data = request.data
        order_list_serializer = self.get_serializer(data=data)

        if not order_list_serializer.is_valid():
            return LResponse(data=order_list_serializer.errors).error(msg="订单参数错误！")

        order_list_serializer.save()

        detail_lst = data.get("detail", [])
        if len(detail_lst) == 0:
            return LResponse().error(msg="订单项不能为空！")

        for detail in detail_lst:
            detail["order_list"] = order_list_serializer.instance.id

        detail_serializer = OrderDetailSerializer(data=detail_lst, many=True)

        if not detail_serializer.is_valid():
            return LResponse().error(msg="订单项参数错误！", data=detail_serializer.errors)

        detail_serializer.save()

        data = {
            'base': order_list_serializer.data,
            'detail': detail_serializer.data
        }

        return LResponse(data).ok()

    @action(methods=["get"], detail=False, url_path="findCountByState", url_name="findCountByState")
    def find_count_by_state(self, request):
        """根据订单状态查询数量"""
        order_state = request.query_params.get("state")
        if not order_state and order_state != 0:
            count = self.queryset.count()
            return LResponse(count).ok()

        return LResponse(0).ok()
