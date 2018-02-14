from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App

from settings import base
from api import routes

app = App(routes=routes.routes,
          settings=base.settings,
          commands=sqlalchemy_backend.commands,  # Install custom commands.
          components=sqlalchemy_backend.components  # Install custom components.
          )

if __name__ == '__main__':
    app.main()
