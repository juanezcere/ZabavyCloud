"""
Datetime Utilities.
"""
import datetime


def now() -> any:
    """
    ? Get the current datetime.
    """
    return datetime.datetime.now()


def utcnow() -> any:
    """
    ? Get the current utc datetime.
    """
    return datetime.datetime.utcnow()


def fromtimestamp(timestamp: int) -> any:
    """
    ? Get the current timestamp.
    """
    return datetime.datetime.fromtimestamp(timestamp)


def strftime(date: datetime.datetime, fmt: str = '%d/%m/%Y %H:%M:%S') -> str:
    return date.strftime(fmt)
