from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from api.core import welcome, yellow, echo_username

routes = [
    Route('/', 'GET', welcome),
    Route('/yellow', 'GET', yellow),
    Route('/{user_id}/', 'GET', echo_username),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
