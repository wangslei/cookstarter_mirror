"""
Django settings for upcooking project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x0h&k^$2i)=fxssim-fpm*vmrb$rs5cz_(y+kzy4^mwzau_g@j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_TOOLBAR_PATCH_SETTINGS = False 
TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'base/templates'),
)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'rest_framework',
    'social_auth',
    'south',
    'base',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
]

ROOT_URLCONF = 'upcooking.urls'

WSGI_APPLICATION = 'upcooking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = False

AUTH_PROFILE_MODULE = 'base.UserProfile'

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

LOGIN_REDIRECT_URL = '/'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
            )


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

#local
FACEBOOK_APP_ID               = '499531130174897'
FACEBOOK_API_SECRET           = '8c07d2d842defe1bbdbd08faa071d7af'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

# APPEND_SLASH = True
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'base.pipeline.custom_load_extra_data',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Parse database configuration from $DATABASE_URL
if os.environ.get("DATABASE_URL", "") != "":
    FACEBOOK_APP_ID               = '502351716559505'
    FACEBOOK_API_SECRET           = '9dbb0b7a3d95af9790b329b46dc0a123'

    import dj_database_url
    DATABASES['default'] =  dj_database_url.config(default='postgres://upcooking:upcooking@localhost:5432/upcooking')

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static asset configuration
