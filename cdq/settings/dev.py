from .base import *
from decouple import config

CORS_ALLOW_HEADERS = ['*']
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

SECRET_KEY = 'django-insecure-b#w^r1ymzxcx@3ohq_i3@ma96psa9!ht4enhje)-96lapq-f%3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DOG_PIC_BUCKET_NAME = config('DOG_PIC_BUCKET_NAME')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = config('AWS_SECRET_KEY')