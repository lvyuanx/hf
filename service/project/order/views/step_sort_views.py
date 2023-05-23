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
        record_obj = StepSortChangeRecord(order_type_id=order_type,
                                          notes=notes)
        record_obj.save()

        step_sort = request.data.get("step_sort")
        for s in step_sort:
            s["change_record"] = record_obj.id
        serializer = self.get_serializer(data=step_sort, many=True)

        if not serializer.is_valid():
            return LResponse(data=serializer.errors).error(msg="订单流程错误！")

        serializer.save()

        StepSortChangeRecord.objects.filter(order_type_id=order_type) \
            .exclude(id=record_obj.id, is_delete=False) \
            .update(is_delete=True)

        return LResponse().ok()
