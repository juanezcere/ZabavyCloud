"""
JWT utilities.
"""
from jwt import decode, encode

from .decorator_utils import tryable

SECRET_KEY: str = '(*)Zabavy=>1.0.0;'
TOKEN_DURATION: int = 21 * 60
ALGORITHM: str = 'HS256'


@tryable
def generate_token(data: any) -> str:
    """
    ? Generates a new token with the given data.
    """
    # logging.debug(f'Generating new token for "{user}".')
    # data = {
    #    'id': user,
    #    'ip': host,
    #    'creation': time(),
    #    'exp': time() + TOKEN_DURATION
    # }
    return encode(data, SECRET_KEY, algorithm=ALGORITHM)


@tryable
def decode_token(token: str) -> any:
    """
    ? Returns the data decoded with the given token.
    """
    return decode(token, SECRET_KEY, algorithms=ALGORITHM)
