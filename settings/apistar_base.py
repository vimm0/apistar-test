# from api.models import Base
from apistar import environment, typesystem

from .base import *
from apistar.parsers import JSONParser

# class Env(environment.Environment):
#     properties = {
#         'DEBUG': typesystem.boolean(default=False),
#         'DATABASE_URL': typesystem.string(default='sqlite:///db.sqlite3')
#     }
#
#
# env = Env()

settings = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',
        'PACKAGE_DIRS': ['apistar']
    },
    # "DATABASE": {
    #     "URL": env['DATABASE_URL'],
    #     "METADATA": Base.metadata
    #
    # },
    'PARSERS': [JSONParser()],
    'SCHEMA': {
        'TITLE': 'User Authentication',
        'DESCRIPTION': 'authentication'
    },
    'TOKEN_AUTHENTICATION': {
        'IS_EXPIRY_TOKEN': True,
        'EXPIRY_TIME': 30,
        'USERNAME_FIELD': 'username',
        'PASSWORD_FIELD': 'password',
        'ORM': 'django',
        'USER_MODEL': 'User',
        'TOKEN_MODEL': 'AccessToken'
    }
}
