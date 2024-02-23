from django.conf.global_settings import CSRF_COOKIE_SECURE

from djangoProject.settings import *

SECRET_KEY = 'django-insecure-7lv*%$+)wvbaft82e2b&o@i3j@z$(@wrv7@$9t5kg&=3fw!5kd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['golshani-ma.ir', 'www.golshnai-ma.ir']

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# STATIC_ROOT = BASE_DIR / 'static'
# MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = '/home/golshani/public_html/static'
MEDIA_ROOT = '/home/golshani/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics"
]
CSRF_COOKIE_SECURE=True
# STATICFILES_DIRS = [
#     BASE_DIR / "statics"
# ]