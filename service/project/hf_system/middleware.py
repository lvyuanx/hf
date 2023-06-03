from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class FilterMenu(MiddlewareMixin):
    def process_request(self, request):  # noqa
        if "/admin/" in request.path:
            # print("访问地址: ", request.path)
            # print("登陆用户: ", request.user)
            # groups = request.user.groups.all()
            # print("用户组: ", groups)
            # # settings.SIMPLEUI_CONFIG['menu_display'] = []
            # for group in :
            #     # 可以根据用户组来groups进行菜单栏管理，可以设置个字典进行配置
            #     # 用户组名和菜单名对应，然后 settings.SIMPLEUI_CONFIG['menu_display'] .append(dict_menu[group.name])就行
            #     print(group.name)
            # # 这里是根据用户名指定不同的菜单
            # if request.user.username == 'user123':
            settings.SIMPLEUI_CONFIG['menu_display'] = ['员工管理', '客户管理']

                # print(settings.SIMPLEUI_CONFIG)
