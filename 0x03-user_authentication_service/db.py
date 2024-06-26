#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        A method used to create a user.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return (user)

    def find_user_by(self, **kwargs) -> User:
        """
        A method to find a user based on a filter.
        """
        keys = list(kwargs)
        first_key = keys[0]
        first_value = kwargs[first_key]
        if first_key not in ['email', 'id', 'session_id']:
            raise InvalidRequestError()
        all_users = self._session.query(User).all()
        if first_key == 'email':
            for user in all_users:
                if first_value == user.email:
                    return user
        elif first_key == 'id':
            for user in all_users:
                if first_value == user.id:
                    return user
        elif first_key == 'session_id':
            for user in all_users:
                if first_value == user.session_id:
                    return user
        raise NoResultFound()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        A method used to update a user.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError()
        self._session.add(user)
        self._session.commit()
