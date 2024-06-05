#!/usr/bin/env python3
"""
A module used to implement basic auth
"""
from api.v1.auth.auth import Auth
import base64
from flask import request


class BasicAuth(Auth):
    """
    A class used to implement basic auth.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Use to extracted base64 from string.
        """
        if authorization_header is None:
            return (None)
        if not isinstance(authorization_header, str):
            return None
        header = authorization_header
        if header.startswith("Basic "):
            return header[len("Basic "):]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        A method used to decode base64.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            byt = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(byt)
            decoded = decoded_bytes.decode('utf-8')
            return decoded
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
