from apistar import annotate
from apistar import render_template
from apistar.backends.django_orm import Session
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated
from apistar.renderers import HTMLRenderer

from apistar_token_auth.authentication import DjangoTokenAuthentication

from .schemas import SignupData


@annotate(renderers=[HTMLRenderer()])
def home():
    """
    Home page that serves <a>index.html</a> template.
    """
    return render_template('index.html')


# CRUD operations in djangoORM
def create_customer(session: Session, name: str, address: str, city: str, state: str):
    """
    Create customer with <u>name, address, city, state fields</u>.
    """
    customer = session.Customer(name=name, address=address, city=city, state=state)
    customer.save()
    return {'id': customer.id, 'name': customer.name, 'address': customer.address, 'city': customer.city,
            'state': customer.state}


def list_customers(session: Session):
    """
       List the available customer.
    """
    queryset = session.Customer.objects.all()
    return [
        {'id': customer.id, 'name': customer.name, 'address': customer.address, 'city': customer.city,
         'state': customer.state}
        for customer in queryset
    ]


# Authentication and Authorization
def logout(session: Session, auth: Auth):
    del session.user.username

    # import ipdb
    # ipdb.set_trace()


@annotate(authentication=[DjangoTokenAuthentication()],
          permissions=[IsAuthenticated()])
def user_profile(session: Session, auth: Auth):
    return {
        'username': auth.user.username
    }


def signup(session: Session, data: SignupData):
    user = session.User(
        username=data['username']
    )
    user.set_password(data['password'])
    user.save()

    return {
        'id': user.id,
        'username': user.username
    }
