from apistar import render_template, annotate
from apistar.interfaces import Template
from apistar.renderers import HTMLRenderer


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
