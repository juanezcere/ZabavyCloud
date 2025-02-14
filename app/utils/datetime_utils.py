"""
Datetime Utilities.
"""
import datetime

Datetime = datetime.datetime


@staticmethod
def now() -> Datetime:
    """
    ? Get the current datetime.
    """
    return datetime.datetime.now()


@staticmethod
def utcnow() -> Datetime:
    """
    ? Get the current utc datetime.
    """
    return datetime.datetime.utcnow()


@staticmethod
def fromtimestamp(timestamp: int) -> Datetime:
    """
    ? Get the current timestamp.
    """
    return datetime.datetime.fromtimestamp(timestamp)


@staticmethod
def strftime(date: Datetime, format: str = "%d/%m/%Y %H:%M:%S") -> str:
    return date.strftime(format)