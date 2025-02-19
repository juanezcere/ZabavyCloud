"""
Decorator utilities.
"""
from .time_utils import duration, sleep, timestamp


def eternal(function: any):
    """
    ? Decorates with a eternal loop function.
    """
    def wrapper(*args, **kwargs):
        while True:
            function(*args, **kwargs)
    return wrapper


def tryable(function: any):
    """
    ? Decorates with a function that tries to runs.
    """
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as err:
            print(f"Error executing function. {err}.")
    return wrapper


def attemptable(tries: int = 1):
    """
    ? Decorates with a function that runs multiple times.
    """
    def decorator(function: any):
        def wrapper(*args, **kwargs):
            for i in range(tries):
                function(*args, **kwargs)
        return wrapper
    return decorator


def demonable(timeout: int = 60000):
    """
    ? Decorates with a infinite function that runs every timeout.
    """
    def decorator(function: any):
        def wrapper(*args, **kwargs):
            print("Starting demon thread.")
            t: int = timestamp()
            while True:
                if duration(start=t) < timeout:
                    sleep()
                    continue
                function(*args, **kwargs)
                t: int = timestamp()
        return wrapper
    return decorator


def timeit(function: any):
    """
    ? Decorates with a function that takes the execution time.
    """
    def wrapper(*args, **kwargs):
        t: int = timestamp()
        function(*args, **kwargs)
        t: float = duration(start=t)
        print(f"Execution time: {t} seconds.")
    return wrapper
