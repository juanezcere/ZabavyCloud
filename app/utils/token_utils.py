"""
Token utilities.
"""
import logging

from jwt import decode, encode

from .time_utils import time

SECRET_KEY: str = '(*)Zabavy=>1.0.0;'
TOKEN_DURATION: int = 21 * 60


def generate_token(user: str, host: str = '0.0.0.0') -> str:
    """
    ? Generates a new token for the user.
    """
    logging.debug(f'Generating new token for "{user}".')
    data = {
        'id': user,
        'ip': host,
        'creation': time(),
        'exp': time() + TOKEN_DURATION
    }
    return encode(data, SECRET_KEY, algorithm='HS256')


def decode_token(token: str) -> dict:
    """
    ? Decodes the given token.
    """
    logging.debug(f'Decoding token "{token}".')
    data = None
    try:
        data = decode(token, SECRET_KEY, algorithms='HS256')
    except Exception as err:
        logging.warning(f'Error decoding the token "{token}". {err}.')
    return data
