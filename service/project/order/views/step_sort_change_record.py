from rest_framework.viewsets import ModelViewSet

from hf_system.utils.response_utils import LResponse
from order.models import StepSortChangeRecord
from order.serializers.step_serializer import StepSortChangeRecordSerializer


class StepSortChangeRecordView(ModelViewSet):
    queryset = StepSortChangeRecord.objects.all()
    serializer_class = StepSortChangeRecordSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        step_sort_change_record = self.get_object()
        if step_sort_change_record.is_delete:
            return LResponse(data=response.data).error(msg="该流程已被删除！")
        serializer = self.get_serializer(instance=step_sort_change_record)
        return LResponse(data=serializer.data).ok()
