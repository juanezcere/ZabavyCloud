from enum import Enum

TITLE:  str = 'Zabavy'
PREVIEW: str = 'https://github.com/juanezcere/Zabavy/blob/feature/reflex-migration/static/preview.png'

METADATA: list = [
    {'name': 'charset', 'content': 'UTF-8'},
    {'name': 'author', 'content': 'Juanez'},
    {'name': 'keywords', 'content': f'{TITLE}, Juanez, Python'},
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'},
    {'name': 'og:type', 'content': 'website'},
    {'name': 'og:image', 'content': PREVIEW},
    {'name': 'twitter:card', 'content': 'summary_large_image'},
    {'name': 'twitter:site', 'content': '@juanez'}
]


class Title(Enum):
    INDEX = f'{TITLE} - Index'
    VARIABLE = f'{TITLE} - Variables'
    SENSOR = f'{TITLE} - Sensors'
    ACTION = f'{TITLE} - Actions'
    ACTUATOR = f'{TITLE} - Actuators'
    DEVICE = f'{TITLE} - Devices'
    GATEWAY = f'{TITLE} - Gateways'


class Description(Enum):
    INDEX = 'Index page description'
    VARIABLE = 'Variables page description'
    SENSOR = 'Sensors page description'
    ACTION = 'Actions page description'
    ACTUATOR = 'Actuators page description'
    DEVICE = 'Devices page description'
    GATEWAY = 'Gateways page description'


class Metadata(Enum):
    INDEX = [
        *METADATA,
        {'name': 'og:title', 'content': Title.INDEX.value},
        {'name': 'og:description', 'content': Description.INDEX.value},
    ]
    VARIABLE = [
        *METADATA,
        {'name': 'og:title', 'content': Title.VARIABLE.value},
        {'name': 'og:description', 'content': Description.VARIABLE.value},
    ]
    SENSOR = [
        *METADATA,
        {'name': 'og:title', 'content': Title.SENSOR.value},
        {'name': 'og:description', 'content': Description.SENSOR.value},
    ]
    ACTION = [
        *METADATA,
        {'name': 'og:title', 'content': Title.ACTION.value},
        {'name': 'og:description', 'content': Description.ACTION.value},
    ]
    ACTUATOR = [
        *METADATA,
        {'name': 'og:title', 'content': Title.ACTUATOR.value},
        {'name': 'og:description', 'content': Description.ACTUATOR.value},
    ]
    DEVICE = [
        *METADATA,
        {'name': 'og:title', 'content': Title.DEVICE.value},
        {'name': 'og:description', 'content': Description.DEVICE.value},
    ]
    GATEWAY = [
        *METADATA,
        {'name': 'og:title', 'content': Title.GATEWAY.value},
        {'name': 'og:description', 'content': Description.GATEWAY.value},
    ]
