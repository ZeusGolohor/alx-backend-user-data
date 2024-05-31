#!/usr/bin/env python3
"""
A script that expects one string argument name
password and returns a salted, hashed password,
which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Use the bcrypt package to perform the hashing.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    A method to that expects 2 arguments and returns a boolean.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
