"""
Platform Utilities.
"""
import platform


def system() -> str:
    """
    ? Returs the system name of the operative system.
    """
    return platform.system()


def release() -> str:
    """
    ? Returs the release of the operative system.
    """
    return platform.release()
