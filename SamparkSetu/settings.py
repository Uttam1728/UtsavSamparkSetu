"""
Django settings for SamparkSetu project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@=5*sn^s%9*3@)0jre$c!o6c3d_rrb227+zs022rj3x@acugn2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MEDIA_URL = '/Photos/'
MEDIA_ROOT = os.path.join(BASE_DIR, "Photos")
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['utsav-sampark-setu.onrender.com', 'drive.google.com', '127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [

    'rangefilter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Yuvak',
    'SamparkKarykar',
    'Mandal',
    'FolloWUp',
    'client_side_image_cropping',
    'more_admin_filters',
    'advanced_filters',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SamparkSetu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

WSGI_APPLICATION = 'SamparkSetu.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'TestSamparkSetu',
#
#         'USER': 'postgres',
#
#         'PASSWORD': '1234',
#
#         'HOST': 'localhost',
#
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'utsav_setu',

        'USER': 'utsav_setu_user',

        'PASSWORD': '7LTgEdab3rj0ncIPFv5lxKMQnTBWdwMh',

        'HOST': 'dpg-cgleo74eoogkndg6ridg-a.oregon-postgres.render.com',

        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'Yuvak/static'),
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_ACCESS_KEY_ID = 'AKIAT7LMKFYQE2NU7K4V'

AWS_S3_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = "samparksetu"

AWS_QUERYSTRING_AUTH = False

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'Yuvak/static/myjs', 'serviceworker.js')
PWA_APP_ICONS = [{'src': '/static/img/utsav.png', 'sizes': '512x512'},
                 {'src': '/static/img/utsav.png', 'sizes': '512x512', "purpose": "maskable"}]
PWA_APP_NAME = 'Utsav Sampark Setu'
PWA_APP_DESCRIPTION = "Utsav Sampark Setu"
PWA_APP_START_URL = '/admin'
# INSTALLED_APPS += ["django_extensions"]
