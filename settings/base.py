# from api.models import Base
# from apistar import environment, typesystem

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'g^9!)y(6=t=*qs$&@nrc(=(^nguojn759#4t(f&0(_bhim!$db'

# class Env(environment.Environment):
#     properties = {
#         'DEBUG': typesystem.boolean(default=False),
#         'DATABASE_URL': typesystem.string(default='sqlite:///db.sqlite3')
#     }
#
#
# env = Env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    'api',
]
settings = {
    # 'DATABASES': {
    #     'default': {
    #         'ENGINE':  'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #         'HOST': '',
    #         'USER': '...',
    #         'PASSWORD': ''
    #     }
    # },
    'TEMPLATES': {
        'ROOT_DIR': 'templates',
        'PACKAGE_DIRS': ['apistar']
    },
    # "DATABASE": {
    #     "URL": env['DATABASE_URL'],
    #     "METADATA": Base.metadata
    #
    # },
}
