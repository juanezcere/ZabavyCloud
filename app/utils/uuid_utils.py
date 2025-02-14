"""
UUID Utilities.
"""
import uuid


@staticmethod
def uuid1() -> str:
    return str(uuid.uuid1())


@staticmethod
def uuid4() -> str:
    return str(uuid.uuid4())


@staticmethod
def generate_id() -> str:
    """
    ? Function to generate unique id from uuid4 without '-'.
    """
    return str(uuid4()).replace('-', '')
