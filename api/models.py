from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Student(Base):
    __tablename__ = "Student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
