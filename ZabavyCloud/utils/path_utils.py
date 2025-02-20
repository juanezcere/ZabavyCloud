"""
Path utilities.
"""
import os


def getcwd() -> str:
    """
    ? Gets the current working directory.
    """
    return os.getcwd()


def join(path: list) -> str:
    """
    ? Joins the given paths.
    """
    return os.path.join(*path)


def exists(path: str) -> bool:
    """
    ? Validates if a file exists in the given path.
    """
    return os.path.exists(path)


def isdir(path: str) -> bool:
    """
    ? Validates if the given path is a folder.
    """
    if exists(path=path):
        return os.path.isdir(path)
    return False


def isfile(path: str) -> bool:
    """
    ? Validates if the given path is a file.
    """
    if exists(path=path):
        return os.path.isfile(path)
    return False


def mkdir(path: str) -> bool:
    """
    ? Creates a directory in the given path.
    """
    if not exists(path=path):
        os.mkdir(path)
        return True
    return False


def rmdir(path: str) -> bool:
    """
    ? Deletes an empty directory in the given path.
    """
    if exists(path=path):
        os.rmdir(path)
        return True
    return False


def remove(path: str) -> bool:
    """
    ? Deletes a file in the given path if exists.
    """
    if exists(path=path):
        os.remove(path)
        return True
    return False


def listdir(path: str, only_files: bool = True) -> list:
    """
    ? Lists the files in the given path.
    """
    if exists(path=path):
        return [f for f in os.listdir(path) if isfile(join(path, f))]
    return []


def splitext(path: str) -> list:
    """
    ? Splites the given path to a list.
    """
    return os.path.splitext(path)


def basename(path: str) -> str:
    """
    ? Gets the file base name of the given path.
    """
    return os.path.basename(path)
