from django.conf.global_settings import CSRF_COOKIE_SECURE

from djangoProject.settings import *

SECRET_KEY = 'django-insecure-7lv*%$+)wvbaft82e2b&o@i3j@z$(@wrv7@$9t5kg&=3fw!5kd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['golshani-ma.ir', 'www.golshnai-ma.ir']

SITE_ID = 3

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'golshani_travel',
        'USER': 'golshani_amin',
        'PASSWORD': '9VBl%CB&RfYw',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# STATIC_ROOT = BASE_DIR / 'static'
# MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = '/home/golshani/public_html/static'
MEDIA_ROOT = '/home/golshani/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics"
]


COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


CSRF_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'
# STATICFILES_DIRS = [
#     BASE_DIR / "statics"
# ]