import os
from pathlib import Path

from django.core.cache.backends.redis import RedisCache

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
STATIC_ROOT = 'D:\\workspace\\project\\git\\hf\\service\\static'
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
    "adminExt",
    "customer",
    "factory",
    "order",
    "web",
    "staff",
    "system",
    "manager"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hf_system.middlewares.simpleui_config_middleware.FilterMenu',
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

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'PASSWORD':'123456',
#         "OPTIONS": {
#             "CLIENT_CLASS": "redis_cache.client.DefaultClient",
#         },
#     },
# }
# REDIS_TIMEOUT=7*24*60*60
# CUBES_REDIS_TIMEOUT=60*60
# NEVER_REDIS_TIMEOUT=365*24*60*60

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

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
#                       '[%(levelname)s][%(message)s]'
#         },
#         'simple': {
#             'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#         },
#         'collect': {
#             'format': '%(message)s'
#         }
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'SF': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 3,  # 备份数为3  xx.log --> xx.log.1 --> xx.log.2 --> xx.log.3
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'TF': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，根据时间自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#             'backupCount': 3,  # 备份数为3  xx.log --> xx.log.2018-08-23_00-00-00 --> xx.log.2018-08-24_00-00-00 --> ...
#             'when': 'D',  # 每天一切， 可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
#             'maxBytes': 1024 * 1024 * 5,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'collect': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'collect',
#             'encoding': "utf-8"
#         }
#     },
#     'loggers': {
#         '': {  # 默认的logger应用如下配置
#             'handlers': ['SF', 'console', 'error'],  # 上线之后可以把'console'移除
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'collect': {  # 名为 'collect'的logger还单独处理
#             'handlers': ['console', 'collect'],
#             'level': 'INFO',
#         }
#     },
# }

LANGUAGE_CODE = 'zh-hans'
USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

default_pwd = '{staff_code}123456'
