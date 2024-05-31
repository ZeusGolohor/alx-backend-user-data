#!/usr/bin/env python3
"""
A scriot to manage personal data.
"""
import os
import logging
import re
from typing import List
import mysql.connector


regx = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """
    A function called filter_datum that returns
    the log message obfuscated.
    """
    extract, replace = (regx["extract"], regx["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


def get_logger() -> logging.Logger:
    """
    Implement a get_logger function that takes no
    arguments and returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    A method to Connect to secure database.
    """
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )
    return connection


def main():
    """
    Implement a main function that takes no
    arguments and returns nothing.
    """
    inputs = "name*email*phone*ssn*password*ip*last_login*user_agent"
    columns = fields.split('*')
    query = "SELECT {} FROM users;".format(inputs)
    logger = get_logger()
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            res = map(
                lambda x: '{}={}'.format(x[0], x[1]),
                zip(columns, row),
            )
            ms = '{};'.format('; '.join(list(res)))
            ag = ("user_data", logging.INFO, None, None, ms, None, None)
            log_record = logging.LogRecord(*ag)
            logger.handle(log_record)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        A method used to format records.
        """
        ms = super(RedactingFormatter, self).format(record)
        res = filter_datum(self.fields, self.REDACTION, ms, self.SEPARATOR)
        return res


if __name__ == "__main__":
    main()
