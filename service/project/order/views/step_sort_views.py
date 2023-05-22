from django.db import transaction
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import LResponse
from order.models import StepSort, StepSortChangeRecord
from order.serializers.StepSerializer import StepSortSerializer


class StepSortView(ModelViewSet):
    queryset = StepSort.objects.all()
    serializer_class = StepSortSerializer

    @action(methods=["post"], detail=False, url_path="edit", url_name="edit")
    @transaction.atomic
    def edit(self, request):
        """修改流程步骤"""
        order_type = request.data.get("order_type")
        notes = request.data.get("notes")
        serializer = self.get_serializer(data=request.data.get("stepSort"), many=True)

        if not serializer.is_valid():
            return LResponse(data=serializer.errors).error(msg="订单流程错误！")

        serializer.save()

        record_obj = StepSortChangeRecord(order_type_id=order_type,
                                          notes=notes,
                                          step_sort_first_id=serializer.data[0]["id"])

        record_obj.save()

        return LResponse().ok()
