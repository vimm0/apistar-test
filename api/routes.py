from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from api.views import home, welcome
# , create_student, retrieve_student, delete_student
from api.views import create_customer, list_customers

routes = [
    Route('/', 'GET', home),
    Route('/welcome', 'GET', welcome),
    # CRUD
    # Route('/create', 'POST', create_student),
    # Route('/retrieve', 'GET', retrieve_student),
    # Route('/update/{student_id}', 'UPDATE', update_student),
    # Route('/delete/{student_id}', 'DELETE', delete_student),

    # CRUD django
    Route('/create', 'POST', create_customer),
    Route('/retrieve', 'GET', list_customers),

    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
