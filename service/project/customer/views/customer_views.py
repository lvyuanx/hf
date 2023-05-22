from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from customer.models import Customer
from customer.serializers.CustomerSerializers import CustomerSerializer
from hf_system.page import CustomPagination
from hf_system.utils.response_utils import LResponse


class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return LResponse(response.data).ok()

    @action(methods=["get"], detail=False, url_path="like", url_name="like")
    def like_list(self, request):
        """模糊查询客户"""
        search: str = request.query_params.get("search")
        paginator = CustomPagination()  # 实例化自定义分页器类
        if not search:
            queryset = self.queryset.all().order_by("-id")

        else:
            queryset = self.queryset.filter(Q(name__icontains=search) |
                                            Q(company_name__contains=search) |
                                            Q(contact_number__contains=search)).order_by('-id')

        results = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(results, many=True)

        return LResponse(serializer.data).page_ok(paginator)
