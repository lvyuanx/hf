import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-&li27w++f8%u=j^yl-e-#&%10vhm$w!1mm*79^0y*n-uw1_4!g'
DEBUG = True

# 文件上传目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 静态文件目录
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'web/static'),
]
# 静态文件映射
STATIC_ROOT = 'D:\\hf_system\\static'

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

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'rest_framework',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "customer",
    "factory",
    "order",
    "web",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    )}

ROOT_URLCONF = 'hf_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hf_system.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hf_system_admin',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'
USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
