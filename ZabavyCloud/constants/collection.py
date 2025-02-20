from enum import Enum


class Collection(Enum):
    VARIABLE = 'variables'
    ACTION = 'actions'
    SENSOR = 'sensors'
    ACTUATOR = 'actuators'
    DEVICE = 'devices'
    GATEWAY = 'gateways'
    MEASURE = 'measures'
