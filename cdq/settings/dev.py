from .base import *

ALLOWED_HOSTS = []

DEBUG = True

SECRET_KEY = 'django-insecure-b#w^r1ymzxcx@3ohq_i3@ma96psa9!ht4enhje)-96lapq-f%3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
