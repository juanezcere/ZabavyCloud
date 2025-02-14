"""
Random utilities.
"""
import random as randomlib


@staticmethod
def random() -> float:
    """
    ? Generates a random number in the range (0.0, 1.0].
    """
    return float(randomlib.random())


@staticmethod
def uniform(minimum: float = 0.0, maximum: float = 1.0) -> float:
    """
    ? Generates a random number in the range (minimum, maximum].
    """
    return float(randomlib.uniform(minimum, maximum))


@staticmethod
def randint(minimum: int = 0, maximum: int = 2) -> int:
    """
    ? Generates an integer random number in range (minimum, maximum].
    """
    return int(randomlib.randint(minimum, maximum))


@staticmethod
def randbool() -> bool:
    """
    ? Generates a bool random number.
    """
    return bool(randint())


@staticmethod
def randbool_percent(percent: float = 1.0) -> bool:
    """
    ? Generates a bool random number.
    """
    return bool(random() >= (1.0 - percent))
