#!/usr/bin/env python3
"""
A script to create a SQLAlchemy model named User
for a database table named users.
"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class User(Base):
    """
    A class to manage the user model.
    """
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=False)
    hashed_password = Column(String(128), nullable=False)
    session_id = Column(String(128))
    reset_token = Column(String(128))

    def __init__(self, *args, **kwargs):
        """
        A method used to initial the user class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = id = str(uuid.uuid4())
            self.email = args[0]
            self.hashed_password = args[1]
