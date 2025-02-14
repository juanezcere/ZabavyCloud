"""
Regular expresion utilities.
"""
import re


@staticmethod
def find_all(pattern: str, text: str) -> list:
    return list(re.findall(pattern, text))


@staticmethod
def search(command: str, pattern: str, text: str) -> str:
    data = re.search(f'{command}{pattern}', text)
    return data.group(0).strip(command).strip() if data else ''


@staticmethod
def validate_is_email(text: str):
    """
    ? Validate that the given text is an email address.
    params:
        ! text: str
            The text to evaluate.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(pattern, text) else False
