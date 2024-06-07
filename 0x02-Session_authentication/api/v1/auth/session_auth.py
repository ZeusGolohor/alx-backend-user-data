#!/usr/bin/env python3
"""
A model to enable session authentication.
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    A class to enable session based authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        A method used to create a session id for user id.
        """
        if user_id is None:
            return (None)
        if not isinstance(user_id, str):
            return (None)
        key = uuid.uuid4()
        self.user_id_by_session_id[str(key)] = user_id
        return (str(key))

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        A method used to retrieve a user id based on session key.
        """
        if session_id is None:
            return (None)
        if not isinstance(session_id, str):
            return (None)
        return (self.user_id_by_session_id.get(session_id))

    def current_user(self, request=None):
        """
        A method used to retreive a user instance via cookies.
        """
        if request is None:
            return (None)
        session_id = self.session_cookie(request)
        if session_id is None:
            return (None)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return (None)
        return (User.get(user_id))

    def destroy_session(self, request=None):
        """
        A method used to delete the user session.
        """
        if request is None:
            return (False)
        cookie = self.session_cookie(request)
        if cookie is None:
            return (False)
        if (self.user_id_for_session_id(cookie) is None):
            return (False)
        del self.user_id_by_session_id[session_cookie]
        return True
