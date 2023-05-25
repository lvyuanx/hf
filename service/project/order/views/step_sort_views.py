from django.db import transaction
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import LResponse
from order.models import StepSort, StepSortChangeRecord
from order.serializers.StepSerializer import StepSortSerializer
from order.utils.utils import sort_ser_steps


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

    @action(methods=["get"], detail=False, url_path="findStepSortByRid", url_name="findStepSortByRid")
    def find_by_rid(self, request):
        """根据record_id查询所有步骤"""
        record_id = request.query_params.get("record_id")
        step_sort_lst = StepSort.objects.filter(change_record_id=record_id)
        serializer = self.get_serializer(instance=step_sort_lst, many=True)
        # 根据parent_step和child_step的关系，生成链表
        step_sort_lst = sort_ser_steps(serializer.data)
        return LResponse(data=step_sort_lst).ok()
