#!/usr/bin/env python3
"""
A script called filter_datum that returns the log message obfuscated.
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    A method called filter_datum that returns the log message obfuscated.
    """
    for field in fields:
        result = re.sub(f'{field}=.*?{separator}',
                        f'{field}={redaction}{separator}', message)
        return (result)
