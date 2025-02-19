"""
Random Utilities.
"""
import random as randomlib


def random() -> float:
    """
    ? Generates a random number in the range (0.0, 1.0].
    """
    return float(randomlib.random())


def uniform(minimum: float = 0.0, maximum: float = 1.0) -> float:
    """
    ? Generates a random number in the range (minimum, maximum].
    """
    return float(randomlib.uniform(minimum, maximum))


def randint(minimum: int = 0, maximum: int = 2) -> int:
    """
    ? Generates an integer random number in range (minimum, maximum].
    """
    return int(randomlib.randint(minimum, maximum))


def randbool() -> bool:
    """
    ? Generates a bool random number.
    """
    return bool(randint())


def randperc(percent: float = 1.0) -> bool:
    """
    ? Generates a bool random at least as percent parameter.
    """
    return bool(random() >= (1.0 - percent))


def choice(elements: list) -> any:
    """
    ? Choice randomly an element of the list.
    """
    return randomlib.choice(elements)


def choices(elements: list, weights: list) -> any:
    """
    ? Choice randomly an element of the list with probability weights.
    """
    return randomlib.choices(elements, weights=weights)


def sample(elements: list, quantity: int) -> any:
    """
    ? Choice a quantity of elements randomly of the list.
    """
    return randomlib.sample(elements, quantity)
