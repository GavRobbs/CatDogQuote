from .base import *
from decouple import config

CORS_ALLOW_HEADERS = ['*']
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cdq',
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

DOG_PIC_BUCKET_NAME = config('DOG_PIC_BUCKET_NAME')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = config('AWS_SECRET_KEY')