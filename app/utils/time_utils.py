"""
Time Utilities.
"""
import time as timelib


@staticmethod
def time() -> float:
    """
    ? Get the current time.
    """
    return float(timelib.time())


@staticmethod
def timestamp() -> int:
    """
    ? Get the current timestamp.
    """
    return int(time() * 1000.0)


@staticmethod
def sleep(duration: float = 1.0) -> None:
    """
    ? Generates a sleep with the duration given (1 second by default).
    """
    timelib.sleep(duration)


@staticmethod
def duration_time(start: float) -> float:
    """
    ? Get the duration from a gived time in seconds.
    """
    return float(time() - start) / 1000.0
