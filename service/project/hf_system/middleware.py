from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from adminExt.configs.label_config import ADMIN_MENU_LABEL, USER_ROLE_LABEL
from adminExt.models import SPremission, SRole
from adminExt.utils.permission_utils import generate_menus


class FilterMenu(MiddlewareMixin):
    def process_request(self, request):  # noqa
        if "/admin/" in request.path:
            menus = []
            # 根据用户权限生成菜单
            if not isinstance(request.user, AnonymousUser):
                user_id = request.user.id
                # 1. 获取菜单根节点
                role = SRole.objects.filter(users=user_id, is_enable=True, is_delete=False,
                                            role_label=USER_ROLE_LABEL).order_by("id")
                if role:
                    curr_user_role = role[0]
                    # 2. 获取菜单LABEL
                    if curr_user_role.role_name == 'admin':
                        label = ADMIN_MENU_LABEL
                    else:
                        label = '%s_%s' % (ADMIN_MENU_LABEL, curr_user_role.role_name)
                    menus = generate_menus(label)
            settings.SIMPLEUI_CONFIG['menus'] = menus if isinstance(menus, list) else menus.get('models')
