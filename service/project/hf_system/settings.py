import os
from pathlib import Path

from hf_system.config import simpleui_config

# ####################### 全局配置 start #######################
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-&li27w++f8%u=j^yl-e-#&%10vhm$w!1mm*79^0y*n-uw1_4!g'
DEBUG = True
# ####################### 全局配置 end #######################

# ####################### 资源配置 start #######################
# 文件上传目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 静态文件目录
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'web/static'),
]
# 静态文件映射
STATIC_ROOT = 'D:\\Project\\git\\hf\\static'
# ####################### 资源配置 end #######################

# ####################### simpleui配置 start #######################
# 去掉默认Logo或换成自己Logo链接
SIMPLEUI_LOGO = simpleui_config.SIMPLEUI_LOGO
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = simpleui_config.SIMPLEUI_HOME_INFO
SIMPLEUI_ANALYSIS = simpleui_config.SIMPLEUI_ANALYSIS
# 隐藏首页的快捷操作和最近动作
SIMPLEUI_HOME_QUICK = simpleui_config.SIMPLEUI_HOME_QUICK
SIMPLEUI_HOME_ACTION = simpleui_config.SIMPLEUI_HOME_ACTION
# 修改首页设置, 指向新创建的控制面板
SIMPLEUI_HOME_PAGE = simpleui_config.SIMPLEUI_HOME_PAGE
SIMPLEUI_HOME_TITLE = simpleui_config.SIMPLEUI_HOME_TITLE
SIMPLEUI_HOME_ICON = simpleui_config.SIMPLEUI_HOME_ICON

# 修改菜单栏配置
SIMPLEUI_CONFIG = simpleui_config.SIMPLEUI_CONFIG
# ####################### simpleui配置 end #######################

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
