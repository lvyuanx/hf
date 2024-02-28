from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseNotFound
from django.utils.deprecation import MiddlewareMixin

from adminExt.const import RoleLabelName, SRoleName, MenuCfg
from manager.models import SRole


class FilterMenu(MiddlewareMixin):
    def process_request(self, request):
        if "/admin/" in request.path:
            if not isinstance(request.user, AnonymousUser):
                user = request.user
                # 获取用户角色
                role_names = SRole.objects.filter(users=user, role_label=RoleLabelName.角色标识.value) \
                    .values_list('role_name', flat=True)
                admin_page_roles = [SRoleName.管理员.value, SRoleName.超级管理员.value]
                if len([role_name for role_name in role_names if role_name in admin_page_roles]) < 0:
                    # 重定向到404页面
                    return HttpResponseNotFound()

                if SRoleName.超级管理员.value in role_names:
                    menu_dict = {}
                    for item in MenuCfg:
                        menu_dict[item.value.get('name')] = item.value
                    settings.SIMPLEUI_CONFIG['menus'] = list(menu_dict.values())
