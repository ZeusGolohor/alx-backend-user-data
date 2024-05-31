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
