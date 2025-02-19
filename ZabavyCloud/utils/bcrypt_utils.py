"""
Bcrypt Utilities.
"""
import bcrypt


def verify_password(password: str, saved_password: str) -> bool:
    """
    ? Verify if both passwords are equals.
    params:
        ! password: str
            The password typed by the user.
        ! saved_password: str
            The password storaged on database.
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password=password_bytes, hashed_password=saved_password)


def get_password_hash(password: str) -> str:
    """
    ? Generates the hash for a password.
    params:
        ! password: str
            The password to generate the hash.
    """
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password
