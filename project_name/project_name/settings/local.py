##################
# LOCAL SETTINGS #
##################

import os

from .base import *


#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


#######################
# CACHE CONFIGURATION #
#######################

# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

INSTALLED_APPS += (
    'debug_toolbar',
)
