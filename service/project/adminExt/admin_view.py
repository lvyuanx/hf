from django.shortcuts import redirect


def defined(request):
    return redirect("/static/index.html")


def generate_menu(request):
    menu = [
        {
            'name': '首页',
            'icon': 'fa fa-home',
            'url': '/',
            'active': True,
        },
        {
            'name': '文章',
            'icon': 'fa fa-file-text-o',
            'sub': [
                {
                    'name': '所有文章',
                    'icon': 'fa fa-list',
                    'url': '/posts/',
                },
                {
                    'name': '添加文章',
                    'icon': 'fa fa-plus',
                    'url': '/posts/add/',
                },
            ]
        },
    ]

    user = request.user

    if user.is_superuser:
        menu.append({
            'name': '管理',
            'icon': 'fa fa-cog',
            'sub': [
                {
                    'name': '用户管理',
                    'icon': 'fa fa-user',
                    'url': '/admin/auth/user/',
                },
                {
                    'name': '组管理',
                    'icon': 'fa fa-users',
                    'url': '/admin/auth/group/',
                },
            ]
        })

    return menu
