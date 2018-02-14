from apistar import render_template, annotate
from apistar.renderers import HTMLRenderer
from apistar.backends import sqlalchemy_backend

from api.models import Student


@annotate(renderers=[HTMLRenderer()])
def home():
    return render_template('index.html')


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


users = {0: 'penny', 1: 'benny', 2: 'jenny'}


def echo_username(user_id: int):
    username = users[user_id]
    return {'message': f'Welcome, {username}!'}


def add_student(db: sqlalchemy_backend, name: str, address: str):
    session = db.session_class()
    student = Student(name=name, address=address)
    print(name)
    session.add(student)
    session.commit()
    return {'name': name }
