from apistar import render_template, annotate
from apistar.renderers import HTMLRenderer
# from apistar.backends.sqlalchemy_backend import Session
from apistar.backends.django_orm import Session

from api.models import Customer


@annotate(renderers=[HTMLRenderer()])
def home():
    """
    Home page that serves <a>index.html</a> template.
    """
    return render_template('index.html')


# CRUD operations

# def create_student(session: Session, name: str, address: str):
#     student = Student(name=name, address=address)
#     session.add(student)
#     session.flush()  # Flush the changes to the database. This will populate the customer id.
#     return {'id': student.id, 'name': student.name, 'address': student.address}
#
#
# def retrieve_student(session: Session):
#     queryset = session.query(Student).all()
#     return [
#         {'id': student.id, 'name': student.name, 'address': student.address}
#         for student in queryset
#     ]
#
#
# # def update_student(session: Session, student_id: int, name: str, address: str):
# #     student = session.query(Student).get(student_id)
# #     Student(id=student, name=name, address=address)
# #     # student = Student(id=student_id, name=name, address=address)
# #     import ipdb
# #     ipdb.set_trace()
# #     session.add(student)
# #     session.flush()  # Flush the changes to the database. This will populate the customer id.
# #     return {'id': student.id, 'name': student.name, 'address': student.address}
#
#
# def delete_student(session: Session, student_id: int):
#     student = session.query(Student).get(student_id)
#     session.delete(student)
#     return {'id': student.id, 'name': student.name, 'address': student.address}

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
        {'id': customer.id, 'name': customer.name}
        for customer in queryset
    ]
