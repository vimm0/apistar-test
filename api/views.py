from apistar import render_template, annotate
from apistar.renderers import HTMLRenderer
from apistar.backends.sqlalchemy_backend import Session

from api.models import Student, Customer


@annotate(renderers=[HTMLRenderer()])
def home():
    return render_template('index.html')


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


# CRUD operations

def create_student(session: Session, name: str, address: str):
    student = Student(name=name, address=address)
    session.add(student)
    session.flush()  # Flush the changes to the database. This will populate the customer id.
    return {'id': student.id, 'name': student.name, 'address': student.address}


def retrieve_student(session: Session):
    queryset = session.query(Student).all()
    return [
        {'id': student.id, 'name': student.name, 'address': student.address}
        for student in queryset
    ]


# def update_student(session: Session, student_id: int, name: str, address: str):
#     student = session.query(Student).get(student_id)
#     Student(id=student, name=name, address=address)
#     # student = Student(id=student_id, name=name, address=address)
#     import ipdb
#     ipdb.set_trace()
#     session.add(student)
#     session.flush()  # Flush the changes to the database. This will populate the customer id.
#     return {'id': student.id, 'name': student.name, 'address': student.address}


def delete_student(session: Session, student_id: int):
    student = session.query(Student).get(student_id)
    session.delete(student)
    return {'id': student.id, 'name': student.name, 'address': student.address}
