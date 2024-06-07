#!/usr/bin/env python3
"""
A model to enable session authentication.
"""
from api.v1.auth.auth import Auth
import uuid


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
