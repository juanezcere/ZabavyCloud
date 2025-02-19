"""
Shutil Utilities.
"""
import shutil

from .path_utils import exists


def copy(path: str, new_path: str) -> bool:
    """
    ? Copies a file or folder to the given new path.
    """
    if exists(path=path):
        shutil.copy(path, new_path)
        return True
    return False


def move(path: str, new_path: str) -> bool:
    """
    ? Moves a file or folder to the given new path.
    """
    if exists(path=path):
        shutil.move(path, new_path)
        return True
    return False
