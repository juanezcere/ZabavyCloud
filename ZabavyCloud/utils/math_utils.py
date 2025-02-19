"""
Mathematic utilities.
"""
import math

PI: float = math.pi
EULER: float = math.e
INF: float = math.inf
NAN: float = math.nan
TAU: float = math.tau


def sin(angle: float) -> float:
    """
    ? Returns the sine of the given angle.
    """
    return math.sin(angle)


def cos(angle: float) -> float:
    """
    ? Returns the cosine of the given angle.
    """
    return math.cos(angle)


def tan(angle: float) -> float:
    """
    ? Returns the tangent of the given angle.
    """
    return math.tan(angle)


def asin(angle: float) -> float:
    """
    ? Returns the asine of the given angle.
    """
    return math.asin(angle)


def acos(angle: float) -> float:
    """
    ? Returns the acosine of the given angle.
    """
    return math.acos(angle)
