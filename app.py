import os

import django

# from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.backends import django_orm

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.apistar_base'

django.setup()

from settings import apistar_base
from api import routes

app = App(routes=routes.routes,
          settings=apistar_base.settings,
          commands=django_orm.commands,  # Install custom commands.
          components=django_orm.components  # Install custom components.
          # commands=sqlalchemy_backend.commands,  # Install custom commands.
          # components=sqlalchemy_backend.components  # Install custom components.
          )

if __name__ == '__main__':
    app.main()
