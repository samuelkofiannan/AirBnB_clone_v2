#!/usr/bin/python3
"""modules imported"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places: places associated with the User
        reviews: reviews the User has made
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
