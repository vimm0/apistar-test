from apistar.frameworks.wsgi import WSGIApp as App

from settings import base
from api import routes

app = App(routes=routes.routes, settings=base.settings)

if __name__ == '__main__':
    app.main()
