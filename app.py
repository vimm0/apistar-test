import os

import django
from django.apps import apps

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.base'

if not apps.ready:
    django.setup()

# from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.backends import django_orm

from settings import base
from api import routes

app = App(routes=routes.routes,
          settings=base.settings,
          commands=django_orm.commands,  # Install custom commands.
          # components=django_orm.components  # Install custom components.
          # commands=sqlalchemy_backend.commands,  # Install custom commands.
          # components=sqlalchemy_backend.components  # Install custom components.
          )

if __name__ == '__main__':
    app.main()
