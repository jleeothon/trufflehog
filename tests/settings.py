# -*- coding: utf-8 -*-

import os

import django


SECRET_KEY = 'fake-key'


INSTALLED_APPS = [
    "tests",
]

WSGI_APPLICATION = 'tests.wsgi.application'

DATABASES = {
    'default': {
    	'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)


# if django.VERSION[:2] < (1, 6):
#     TEST_RUNNER = 'discover_runner.DiscoverRunner'
