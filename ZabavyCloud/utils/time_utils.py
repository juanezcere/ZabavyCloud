"""
Time Utilities.
"""
import time as timelib


def time() -> float:
    """
    ? Get the current time.
    """
    return float(timelib.time())


def timestamp() -> int:
    """
    ? Get the current timestamp.
    """
    return int(time() * 1000.0)


def sleep(duration: float = 1.0) -> None:
    """
    ? Generates a sleep with the duration given (1 second by default).
    """
    timelib.sleep(duration)


def duration(start: float = 0.0) -> float:
    """
    ? Get the duration from a gived time in milliseconds.
    """
    return float(time() - start) / 1000.0
