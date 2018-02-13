def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def yellow(question=None):
    if question is None:
        return {'message': 'Hey yellow message'}


users = {0: 'penny', 1: 'benny', 2: 'jenny'}


def echo_username(user_id: int):
    username = users[user_id]
    return {'message': f'Welcome, {username}!'}
