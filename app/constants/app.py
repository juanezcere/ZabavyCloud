NAME: str = 'Zabavy'
TITLE: str = 'Zabavy'
VERSION: str = '1.0.0'
LOG_LEVEL: int = 10

ICON: str = 'zabavy.png'
AUTHOR: str = 'Juanez'
REPOSITORY_URL: str = 'https://github.com/juanezcere/Zabavy'
CONTACT_URL: str = 'https://github.com/juanezcere'
CONTACT_EMAIL: str = 'juanezcere@gmail.com'

API_VERSION: str = '1.0.0'
DESCRIPTION: str = 'Esta API ofrece una solución completa para la gestión de usuarios, permisos y roles, proporcionando una interfaz intuitiva para la subida de archivos y una interfaz gráfica que facilita la interacción con los datos. Su diseño modular permite una fácil integración con diferentes sistemas y aplicaciones, brindando flexibilidad y escalabilidad para adaptarse a las necesidades específicas de cada proyecto.'
SUMMARY: str = 'Esta API es una herramienta poderosa y versátil que le permitirá gestionar de manera eficiente y segura usuarios, permisos, roles, archivos y datos en sus proyectos. Su diseño modular y su interfaz gráfica intuitiva la convierten en una solución ideal para una amplia gama de aplicaciones.'
HOST: str = '0.0.0.0'
PORT: int = 8000

LICENCE_INFO: dict = {
    'name': 'Apache 2.0',
    'identifier': 'MIT',
}


API_CONTACT: dict = {
    'name': AUTHOR,
    'url': CONTACT_URL,
    'email': CONTACT_EMAIL,
}

ORIGINS: list = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:8080',
]

WEB_VERSION: str = '1.0.0'

HEADERS: dict = {
    'Content_Type': 'application/json',
    'Accept': 'application/json',
}

EMAIL_EXAMPLE: str = 'user@example.com'
