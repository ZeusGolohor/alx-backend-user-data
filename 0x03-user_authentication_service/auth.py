#!/usr/bin/env python3
"""
A script to handle user auth.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    A method used to hash user password.
    """
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_pwd


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    def __init__(self):
        """
        Used to initialize the class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        A method used to register a new user
        """
        try:
            check_user = self._db.find_user_by(email=email)
            if check_user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            user = self._db.add_user(
                                     email=email,
                                     hashed_password=_hash_password(password))
            return (user)

    def valid_login(self, email: str, password: str) -> bool:
        """
        A method used to valid a user's password.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(
                                      password.encode('utf-8'),
                                      user.hashed_password)
        except NoResultFound:
            return (False)
