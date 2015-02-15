#################
# BASE SETTINGS #
#################

import os

from django.core.exceptions import ImproperlyConfigured


###########
# HELPERS #
###########

def get_env_setting(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = ('The {} env variable was not found '
                         'and no default was set!').format(setting)
            raise ImproperlyConfigured(error_msg)


######################
# PATH CONFIGURATION #
######################

# Absolute filesystem path to the Django project directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Absolute filesystem path to the top-level project folder
SITE_DIR = os.path.dirname(BASE_DIR)


#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = 'this_is_my_development_key'


#####################
# APP CONFIGURATION #
#####################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#installed-apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

PROJECT_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS


############################
# MIDDLEWARE CONFIGURATION #
############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


#####################
# URL CONFIGURATION #
#####################

ROOT_URLCONF = '{{ project_name }}.urls'


######################
# WSGI CONFIGURATION #
######################

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


#########################
# GENERAL CONFIGURATION #
#########################

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#use-tz
USE_TZ = True


##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(SITE_DIR, 'templates'),
)


#############################
# STATIC FILE CONFIGURATION #
#############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#static-root
STATIC_ROOT = os.path.join(SITE_DIR, 'assets')

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(SITE_DIR, 'static'),
)


############################
# MEDIA FILE CONFIGURATION #
############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#media-root
MEDIA_ROOT = os.path.join(SITE_DIR, 'media')

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#media-url
MEDIA_URL = '/media/'


############################
# WHITENOISE CONFIGURATION #
############################

# http://whitenoise.evans.io/en/latest/django.html#add-gzip-and-caching-support
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#############################
# PROJECT SPECIFIC SETTINGS #
#############################

# Project specific additions go here!
