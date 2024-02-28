from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from adminExt.const import RoleLabelName, StaffType
from manager.models import SRole, SRoleLabel
from manager.serializers.manager import SRoleSerializer, SRoleLiteListSerializer
from hf_system.utils.response_utils import LResponse


class SRoleView(ModelViewSet):
    queryset = SRole.objects.all()
    serializer_class = SRoleSerializer

    @action(methods=["get"], detail=False, url_path="lite/list", url_name="role_lite_list")
    def edit(self, request):
        manage = self.queryset.filter(role_label=RoleLabelName.员工类型标识.value)\
            .exclude(role_name=StaffType.BOSS.value).values('id', 'notes')
        serializer = SRoleLiteListSerializer(manage, many=True)

        return LResponse(serializer.data).ok()
