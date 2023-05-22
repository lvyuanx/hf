SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['客户管理', '工厂管理', '订单管理', '权限认证'],
    'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
            'name': '客户管理',
            'icon': 'fas fa-address-book',
            'models': [{
                'name': '客户列表',
                'icon': 'fa fa-list',
                'url': 'customer/customer/'
            }]

        },
        {
            'name': '工厂管理',
            'icon': 'fas fa-cog',
            'models': [{
                'name': '模具列表',
                'icon': 'fa fa-list',
                'url': 'factory/modelinfo/'
            }]

        },
        {
            'name': '订单管理',
            'icon': 'fas fa-bell',
            'models': [
                {
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
                            'url': 'order/stepsort/'
                        }
                    ]
                },
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

        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [{
                'name': '用户',
                'icon': 'fa fa-user',
                'url': 'auth/user/'
            }]

        }
    ]
}

# 去掉默认Logo或换成自己Logo链接
SIMPLEUI_LOGO = '/media/logo/logo.jpg'
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
# 隐藏首页的快捷操作和最近动作
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_ACTION = False
# 修改首页设置, 指向新创建的控制面板
SIMPLEUI_HOME_PAGE = '/admin/defined/#/dashboard'
SIMPLEUI_HOME_TITLE = '控制面板'
SIMPLEUI_HOME_ICON = 'fa fa-eye'
