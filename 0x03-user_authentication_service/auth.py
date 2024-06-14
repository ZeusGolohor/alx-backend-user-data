#!/usr/bin/env python3
"""
A script to handle user auth.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    A method used to hash user password.
    """
    salt = bcrypt.gensalt()
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_pwd
