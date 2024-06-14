#!/usr/bin/env python3
"""
A script to create a SQLAlchemy model named User
for a database table named users.
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class User(Base):
    """
    A class to manage the user model.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
