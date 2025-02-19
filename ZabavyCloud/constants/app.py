"""
Constants for the app.
"""
# App
APP_NAME: str = 'Zabavy'
APP_TITLE: str = 'Zabavy Cloud'
APP_ICON: str = 'zabavy.png'
APP_VERSION: str = '1.0.0'

LOG_LEVEL: int = 10

APP_AUTHOR: str = 'Juanez'
APP_CONTACT_URL: str = 'https://github.com/juanezcere'
APP_CONTACT_EMAIL: str = 'juanezcere@gmail.com'

APP_DESCRIPTION: str = 'App description'
APP_SUMMARY: str = 'App summary'

HOST: str = '0.0.0.0'
API_VERSION: str = '1.0.0'
API_PORT: int = 8000
WEB_VERSION: str = '1.0.0'
WEB_PORT: int = 3000

API_CONTACT: dict = {
    'name': APP_AUTHOR,
    'url': APP_CONTACT_URL,
    'email': APP_CONTACT_EMAIL,
}

LICENCE_INFO: dict = {
    'name': 'Apache 2.0',
    'identifier': 'MIT',
}

SOFTWARE_VERSION: str = '1.0.0'
HARDWARE_VERSION: str = '1.0.0'


# Folders
DATA_FOLDERS: dict = {
    'assets': 'assets',
    'logs': '.logs',
    'temp': '.temp',
    'static_assets': 'assets/static',
    'images': 'assets/images',
}
