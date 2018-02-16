# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
#
# Base = declarative_base()
#
#
# class Student(Base):
#     __tablename__ = "Student"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     address = Column(String)
#
#
# class Customer(Base):
#     __tablename__ = "Customer"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#

from django.db import models


class AccessToken(models.Model):
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)

    class Meta:
        app_label = 'api'

# class Student(models.Model):
#     pass
