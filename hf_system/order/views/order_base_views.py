from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from hf_system.page import CustomPagination
from hf_system.utils.response_utils import page_ok, response_error, response_ok, LResponse
from order.models import OrderBase
from order.serializers.OrderSerializer import OrderBaseSerializer, OrderListSerializer


class OrderBaseView(ModelViewSet):
    queryset = OrderBase.objects.all()
    serializer_class = OrderBaseSerializer

    def retrieve(self, request, *args, **kwargs):
        """获取订单基础信息"""
        response = super().retrieve(request, *args, **kwargs)
        return LResponse(response.data).ok()

    @action(methods=["get"], detail=False, url_path="like", url_name="like")
    def like_list(self, request):
        """模糊查询款号"""
        code_or_name: str = request.query_params.get("code_or_name")
        paginator = CustomPagination()  # 实例化自定义分页器类
        if not code_or_name:
            queryset = self.queryset.all().order_by('-id')

        else:
            queryset = self.queryset.filter(Q(order_code__icontains=code_or_name) |
                                            Q(order_product__icontains=code_or_name)).order_by("-id")

        results = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(results, many=True)

        return LResponse(serializer.data).page_ok(paginator)

