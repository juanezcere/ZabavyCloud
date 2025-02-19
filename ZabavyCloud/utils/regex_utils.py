"""
Regular Expresion Utilities.
"""
import re


def findall(pattern: str, text: str) -> list:
    """
    ? Finds all the matchs of the given pattern in the text.
    """
    return list(re.findall(pattern, text))


def search(pattern: str, text: str) -> list:
    """
    ? Search all the matchs of the given pattern in the text.
    """
    return list(re.search(pattern, text))


def search_command(command: str, pattern: str, text: str) -> str:
    data = re.search(f'{command}{pattern}', text)
    return data.group(0).strip(command).strip() if data else ''


def validate_is_email(text: str):
    """
    ? Validate that the given text is an email address.
    params:
        ! text: str
            The text to evaluate.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(pattern, text) else False
