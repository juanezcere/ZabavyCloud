"""
Serial utilities.
"""
import logging

import serial

from .time_utils import sleep


@staticmethod
def create_serial_port(port: str, baudrate: int = serial.Serial.BAUDRATES[12], bytesize: int = serial.Serial.BYTESIZES[3], parity: str = serial.Serial.PARITIES[0], stopbits: float = serial.Serial.STOPBITS[0], timeout: float = 1.0) -> serial.Serial | None:
    """
    Creates a serial port.
    """
    logging.debug(f'Trying to connect to serial port "{port}".')
    try:
        return serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, timeout=timeout)
    except Exception as err:
        logging.error(f'Cannot connect to serial port "{port}". {err}.')
    return None


@staticmethod
def find_serial_ports() -> list:
    """
    Detects the available serial ports in device.
    """
    logging.debug('Looking for available serial ports.')
    ports: list = [f'/dev/tty{port}{number}' for port in ['S', 'AMA', 'USB'] for number in range(5)]
    serial_ports: list = []
    for port in ports:
        logging.debug(f'Connecting to port "{port}".')
        serial_port = create_serial_port(port=port)
        sleep(duration=0.1)
        if serial_port is None:
            continue
        if not serial_port.is_open:
            logging.warning(f'The port "{port}" is already open.')
            continue
        serial_port.close()
        logging.info(f'LoRa module found at the port "{port}".')
        serial_ports.append(port)
    return serial_ports


@staticmethod
def find_lora_serial_ports(ports: list = []) -> list:
    """
    Detects the LoRa modules attached to any serial port.
    """
    logging.debug('Looking for available LoRa serial ports.')
    serial_ports: list = []
    for port in ports:
        logging.debug(f'Finding LoRa module at port "{port}".')
        serial_port = create_serial_port(port=port)
        sleep(duration=0.1)
        if serial_port is None:
            continue
        if not serial_port.is_open:
            logging.warning(f'The port "{port}" is already open.')
            continue
        serial_port.flush()
        sleep(duration=0.1)
        logging.debug(f'Sending "AT" command to the port "{port}".')
        serial_port.write('AT'.encode())
        for _ in range(5):
            sleep(duration=0.1)
            if not serial_port.inWaiting:
                continue
            try:
                response: str = serial_port.read(128).decode()
                resp: list = [r in response for r in ['OK']]
                if not any(resp):
                    continue
                logging.info(f'LoRa module found at the port "{port}".')
                serial_ports.append(port)
                break
            except Exception as err:
                logging.warning(f'The serial port "{port}" is not a LoRa module. {err}.')
        serial_port.close()
    return serial_ports
