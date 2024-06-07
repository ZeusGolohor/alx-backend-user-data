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
        if path is None:
            return (True)
        if excluded_paths is None:
            return (True)
        if len(excluded_paths) == 0:
            return (True)
        if path[-1] != '/':
            path += '/'
        for route in excluded_paths:
            if path == route:
                return (False)
        return (True)

    def authorization_header(self, request=None) -> str:
        """
        Use to determine authentication header.
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """"
        Use to return the current user.
        """
        return None
