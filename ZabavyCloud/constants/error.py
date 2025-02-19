from enum import Enum


class Error(Enum):
    SUCCESSFULLY = {
        'code': '000',
        'message': 'successfully_executed'
    }

    INVALID_TOKEN = {'code': '001', 'message': 'invalid_token'}
    INVALID_EMAIL_ADDRESS = {'code': '002', 'message': 'invalid_email_address'}
    INCORRECT_CREDENTIALS = {'code': '003', 'message': 'incorrect_credentials'}
    USER_NOT_EXISTS = {'code': '004', 'message': 'user_not_exists'}
    USER_ALREADY_EXISTS = {'code': '005', 'message': 'user_already_exists'}
    PERMISSION_NOT_EXISTS = {'code': '006', 'message': 'permission_not_exists'}
    PERMISSION_ALREADY_EXISTS = {'code': '007',
                                 'message': 'permission_already_exists'}

    VARIABLE_NOT_EXISTS = {
        'code': '010',
        'message': 'variable_not_exists'
    }
    VARIABLE_ALREADY_EXISTS = {
        'code': '011',
        'message': 'variable_already_exists'
    }
    ACTION_NOT_EXISTS = {
        'code': '012',
        'message': 'action_not_exists'
    }
    ACTION_ALREADY_EXISTS = {
        'code': '013',
        'message': 'action_already_exists'
    }
    SENSOR_NOT_EXISTS = {
        'code': '014',
        'message': 'sensor_not_exists'
    }
    SENSOR_ALREADY_EXISTS = {
        'code': '015',
        'message': 'sensor_already_exists'
    }
    ACTUATOR_NOT_EXISTS = {
        'code': '016',
        'message': 'actuator_not_exists'
    }
    ACTUATOR_ALREADY_EXISTS = {
        'code': '017',
        'message': 'actuator_already_exists'
    }
    DEVICE_NOT_EXISTS = {
        'code': '018',
        'message': 'device_not_exists'
    }
    DEVICE_ALREADY_EXISTS = {
        'code': '019',
        'message': 'device_already_exists'
    }
    GATEWAY_NOT_EXISTS = {
        'code': '020',
        'message': 'gateway_not_exists'
    }
    GATEWAY_ALREADY_EXISTS = {
        'code': '021',
        'message': 'gateway_already_exists'
    }
