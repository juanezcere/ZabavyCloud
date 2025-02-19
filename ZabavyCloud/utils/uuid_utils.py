"""
UUID Utilities.
"""
import uuid


def uuid1() -> str:
    """
    ? Generates uuid1.
    """
    return str(uuid.uuid1())


def uuid4() -> str:
    """
    ? Generates uuid4.
    """
    return str(uuid.uuid4())


def generate_id() -> str:
    """
    ? Function to generate unique id from uuid4 without '-'.
    """
    return str(uuid4()).replace('-', '')
