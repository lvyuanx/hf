import copy
import json

from adminExt.models import SPremission
from adminExt.serializers.admin_ext import SPremissionSerializer


def generate_menus(label):
    """
    生成菜单
    :param label: 权限标识
    :return:
    """
    # 1. 获取所有的菜单
    menus_set = SPremission.objects.filter(permission_label=label, is_enable=True, is_delete=False).order_by("id")
    if not menus_set:
        return []

    # 2. 序列化菜单
    serializer_menus = SPremissionSerializer(menus_set, many=True)
    menus = serializer_menus.data

    # 3. 生成菜单树
    root_menu = None
    for menu in menus:
        if not menu["parent"]:
            root_menu = menu
            break
    if not root_menu:
        return []
    menus_tree = generate_menus_tree(menus, root_menu)
    format_menu_tree = format_menus(menus_tree)
    return format_menu_tree


def generate_menus_tree(menus, root_menu):
    """
    递归生成菜单树
    :param menus: 菜单列表
    :param root_menu: 根菜单
    :return: meuus_tree
    """
    # 1. 获取根菜单
    if not root_menu:
        root_menu = copy.deepcopy(menus[0])
        menus.pop(0)

    # 2. 获取子菜单
    child_menus = []
    for menu in menus:
        if menu["parent"] == root_menu["id"]:
            child_menus.append(menu)

    # 3. 递归生成子菜单
    for child_menu in child_menus:
        generate_menus_tree(menus, child_menu)

    # 4. 将子菜单添加到根菜单中
    root_menu["models"] = child_menus

    return root_menu


def format_menus(menu_tree):
    """
    格式化菜单
    :param menu_tree: 菜单
    :return: {
        'name': '员工管理',
        'icon': 'fas fa-address-book',
        'models': [{
            'name': '员工列表',
            'icon': 'fa fa-list',
            'url': 'staff/staffbase/'
        }]

    }
    """
    if isinstance(menu_tree, list):
        return [format_menus(menu) for menu in menu_tree]
    menu = {"name": menu_tree["permission_name"],
            "icon": menu_tree.get("menu_icon", ""),
            "url": menu_tree.get("menu_url", "")}
    if menu_tree.get("models"):
        menu['models'] = format_menus(menu_tree["models"])
    return menu
