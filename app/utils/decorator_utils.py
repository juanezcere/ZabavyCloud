"""
Decorator utilities.
"""
import logging

from .time_utils import sleep, timestamp


def demon_decorator(timeout: int = 60000):
    """
    ? Decorates with a infinite function that runs every timeout.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            logging.debug("Starting demon thread.")
            t: int = timestamp()
            while True:
                if timestamp() - t < timeout:
                    sleep()
                    continue
                # logging.debug("Updating demon thread.")
                function(*args, **kwargs)
                t: int = timestamp()
        return wrapper
    return decorator


def attempt_decorator(tries: int = 1):
    """
    ? Decorates with a function that runs multiple times.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                if function(*args, **kwargs):
                    break
        return wrapper
    return decorator


def tryable_decorator(function):
    """
    ? Decorates with a function that tries to runs.
    """
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as err:
            logging.warning(f"Error executing function. {err}.")
    return wrapper


def loop_decorator(function):
    """
    ? Decorates with a loop function.
    """
    def wrapper(*args, **kwargs):
        while True:
            return function(*args, **kwargs)
    return wrapper


def time_decorator(function):
    """
    ? Decorates with a function that counts the execution time.
    """
    def wrapper(*args, **kwargs):
        t: int = timestamp()
        function(*args, **kwargs)
        t: float = (timestamp() - t) / 1000.0
        logging.info(f"Execution time: {t} seconds.")
    return wrapper
