#coding:utf-8 
"""
Django settings for MoocKitchen project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
import os.path
#import sae.const
from os import environ
debug = not environ.get("APP_NAME", "")
# if debug:
#LOCAL 本地调试用，便于导出数据库,根据本地MYSQL数据库填写下面参数<----------------如果文件中出现中文，一定要在开始添加 #coding:utf-8
MYSQL_DB = 'kitchen'
MYSQL_USER = 'root'
MYSQL_PASS = '..xiao'
MYSQL_HOST_M = '127.0.0.1'
MYSQL_HOST_S = '127.0.0.1'
MYSQL_PORT = '3306'
# else:
#SAE
    # import sae.const
    # from sae._restful_mysql import monkey
    # monkey.patch()
    # MYSQL_DB = sae.const.MYSQL_DB
    # MYSQL_USER = sae.const.MYSQL_USER
    # MYSQL_PASS = sae.const.MYSQL_PASS
    # MYSQL_HOST_M = sae.const.MYSQL_HOST
    # MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    # MYSQL_PORT = sae.const.MYSQL_PORT

DEFAULT_CHARSET = 'utf-8'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j25%%awr4-@25wn$34@owq$ht2fx$1q+ct^4-2m%mq7m$!#2xc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Mooc',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'MoocKitchen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
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

WSGI_APPLICATION = 'MoocKitchen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'

FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520
FILE_UPLOAD_TEMP_DIR = '/s/mooc/tmp/'
#---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#MEDIA_ROOT= os.path.join(BASE_DIR,'Mooc/static/files/CourseImg')
MEDIA_ROOT = os.path.join(BASE_DIR,'Mooc/static')
MEDIA_URL = '/files/'
#---------------------------------------------------
print(MEDIA_ROOT)
print("Hello")