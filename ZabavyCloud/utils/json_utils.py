"""
JSON Utilities.
"""
import json


def json_to_string(data: dict) -> str:
    """
    ? Creates a string from a dictionary.
    """
    return json.dumps(data, indent=4, ensure_ascii=False)


def string_to_json(data: dict) -> dict:
    """
    ? Creates a dictionary from a string.
    """
    return json.loads(data)


def load_json(file: str) -> dict:
    """
    ? Loads a dictionary from a json file.
    """
    data: dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        data: dict = string_to_json(f.read())
    return data


def write_json(file: str, data: dict) -> None:
    """
    ? Creates a file with the given dictionary.
    """
    with open(file, 'w', encoding='utf-8') as f:
        f.write(json_to_string(data))
