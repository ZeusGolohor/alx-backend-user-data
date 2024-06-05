#!/usr/bin/env python3
"""
A module to handle authentication.
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    A class to handle authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        To determine if authentication is required.
        """
        return (False)

    def authorization_header(self, request=None) -> str:
        """
        Use to determine authentication header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"
        Use to return the current user.
        """
        return (None)
