"""
Path utilities.
"""
from os import mkdir, remove, rmdir
from os.path import exists, join
from shutil import copyfile


@staticmethod
def join_directory(path: list) -> str:
    """
    ? Joins the given paths.
    """
    return join(*path)


@staticmethod
def create_directory(path: str) -> bool:
    """
    ? Creates a directory in the given path.
    """
    if not exists(path):
        mkdir(path)
        return True
    return False


@staticmethod
def delete_directory(path: str) -> bool:
    """
    ? Deletes an empty directory in the given path.
    """
    if exists(path):
        rmdir(path)
        return True
    return False


@staticmethod
def delete_file(path: str) -> bool:
    """
    ? Deletes a file in the given path if exists.
    """
    if exists(path):
        remove(path, new_path)
        return True
    return False


@staticmethod
def copy_file(path: str, new_path: str) -> bool:
    """
    ? Creates a copy of a file in the given new path.
    """
    if exists(path):
        copyfile(path, new_path)
        return True
    return False
