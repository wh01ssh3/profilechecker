from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'profilechecker',
        'USER': 'profilechecker',
        'PASSWORD': 'profilechecker',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
