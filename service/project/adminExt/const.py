from enum import Enum


class RoleLabelName(Enum):
    """角色标签名称"""
    角色标识 = 'SROLE'
    员工类型标识 = 'STAFF_TYPE'


class SRoleName(Enum):
    """系统内管角色名称"""
    超级管理员 = 'SUPER_ADMIN'  # 拥有一切权限
    管理员 = 'ADMIN'  # 允许进入后台
    用户 = 'USER'  # 普通用户
    员工 = 'STAFF'  # 员工


class StaffType(Enum):
    """员工类型"""
    BOSS = 'BOSS'
    厂长 = 'FACTORY_DIRECTOR'
    业务跟单 = 'YWGD'
    生产跟单 = 'SCGD'


class MenuCfg(Enum):
    员工管理 = {
        'name': '员工管理',
        'icon': 'fas fa-address-book',
        'models': [{
            'name': '员工列表',
            'icon': 'fa fa-list',
            'url': 'staff/staffbase/'
        }]

    }
    客户管理 = {
        'name': '客户管理',
        'icon': 'fas fa-address-book',
        'models': [{
            'name': '客户列表',
            'icon': 'fa fa-list',
            'url': 'customer/customer/'
        }]

    }
    工厂管理 = {
        'name': '工厂管理',
        'icon': 'fas fa-cog',
        'models': [{
            'name': '模具列表',
            'icon': 'fa fa-list',
            'url': 'factory/modelinfo/'
        }]

    }

    流程管理 = {
        'name': '流程管理',
        'icon': 'el-icon-guide',
        'models': [
            {
                'name': '流程列表',
                'icon': 'fa fa-list',
                'url': 'order/stepbase/'
            },
            {
                'name': '订单流程管理',
                'icon': 'el-icon-paperclip',
                'url': 'order/stepsortchangerecord/'
            }
        ]
    }

    订单管理 = {
        'name': '订单管理',
        'icon': 'fas fa-bell',
        'models': [
            {
                'name': '订单类型',
                'icon': 'fa fa-calendar',
                'url': 'order/ordertype/'
            },
            {
                'name': '订单款号',
                'icon': 'fa fa-heart',
                'url': 'order/orderbase/'
            },
            {
                'name': '订单列表',
                'icon': 'fa fa-list',
                'url': 'order/orderlist/'
            },
        ]

    }

    权限管理 = {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [
            {
                'name': '用户',
                'icon': 'fa fa-user',
                'url': 'auth/user/'
            },
            {
                'name': '用户组',
                'icon': 'fa fa-th-list',
                'url': 'auth/group/'
            }

        ]
    }


staff_menu_cfg = {
    StaffType.BOSS.value: [MenuCfg.权限管理.value, MenuCfg.流程管理.value],
    StaffType.厂长.value: [MenuCfg.员工管理.value,
                           MenuCfg.客户管理.value,
                           MenuCfg.工厂管理.value,
                           MenuCfg.订单管理.value],
    StaffType.业务跟单.value: [MenuCfg.客户管理.value],
}
