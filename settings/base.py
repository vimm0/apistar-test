from api.models import Base
from apistar import environment, typesystem


class Env(environment.Environment):
    properties = {
        'DEBUG': typesystem.boolean(default=False),
        'DATABASE_URL': typesystem.string(default='sqlite:///db.sqlite3')
    }


env = Env()

settings = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',
        'PACKAGE_DIRS': ['apistar']
    },
    "DATABASE": {
        "URL": env['DATABASE_URL'],
        "METADATA": Base.metadata

    }
}
