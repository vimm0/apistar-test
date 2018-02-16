from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from apistar_token_auth.handlers import django_get_token

from api.alchemy.views import create_student, retrieve_student, delete_student
from api.orm.views import home, create_customer, list_customers
from api.orm.views import user_profile, signup, logout

routes = [
    Route('/', 'GET', home),

    # CRUD SQLAlchemy
    Route('/create', 'POST', create_student),
    Route('/retrieve', 'GET', retrieve_student),
    # Route('/update/{student_id}', 'UPDATE', update_student),
    Route('/delete/{student_id}', 'DELETE', delete_student),

    # CRUD djangoORM
    Route('/create', 'POST', create_customer),
    Route('/retrieve', 'GET', list_customers),
    # apistar_token_authentication
    Route('/token', 'POST', django_get_token, 'token-login'),
    Route('/profile', 'GET', user_profile, 'User-Profile'),
    Route('/signup', 'POST', signup, 'Signup'),
    Route('/logout', 'POST', logout, 'logout'),

    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
