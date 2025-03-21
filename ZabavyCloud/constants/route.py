from enum import Enum


class Route(Enum):
    INDEX = '/'

    VARIABLE = '/variables'
    ACTION = '/actions'
    SENSOR = '/sensors'
    ACTUATOR = '/actuators'
    DEVICE = '/devices'
    GATEWAY = '/gateways'
    MEASURE = '/measures'

    LOGIN = '/login'
    LOGOUT = '/logout'
    RESTORE = '/restore'
    SIGNUP = '/signup'
    PASSWORD = '/password'
    ACTIVATE = '/activate'
    HOME = '/home'
    USER = '/users'
    PERMISSION = '/permissions'
