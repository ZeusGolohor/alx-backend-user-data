#!/usr/bin/env python3
"""
A script called filter_datum that returns the log message obfuscated.
"""
from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    A method called filter_datum that returns the log message obfuscated.
    """
    for field in fields:
        result = re.sub(f'{field}=.*?{separator}',
                        f'{field}={redaction}{separator}', message)
        return (result)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        A method to filter values in incoming log records
        using filter_datum. Values for fields in fields
        should be filtered.
        """
        return filter_datum(self.fields, self.REDACTION,
                            record.getMessage(), self.SEPARATOR)