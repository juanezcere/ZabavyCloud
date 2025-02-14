"""
Terminal utilities.
"""
import logging
from os import popen, system

from .time_utils import sleep


@staticmethod
def reboot() -> None:
    logging.info('Rebooting the system.')
    try:
        system('sudo reboot')
    except Exception as err:
        logging.warning(f'Warning rebooting the system. {err}.')


@staticmethod
def restart_usb() -> None:
    logging.info('Restarting USB ports.')
    try:
        system('sudo rmmod xhci_pci')
        sleep(duration=2)
        system('sudo modprobe xhci_pci')
        sleep(duration=1)
    except Exception as err:
        logging.warning(f'Warning restarting USB ports. {err}.')


@staticmethod
def restart_network(interface) -> None:
    logging.info('Restarting network.')
    try:
        system(f'sudo ifconfig {interface} down')
        sleep(duration=2)
        system(f'sudo ifconfig {interface} up')
        sleep(duration=1)
    except Exception as err:
        logging.warning(f'Warning restarting network. {err}.')


@staticmethod
def update_datetime() -> None:
    logging.info('Updating datetime.')
    try:
        system('sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d" " -f5-8)Z"')
    except Exception as err:
        logging.warning(f'Warning updating datetime. {err}.')


@staticmethod
def get_network_interfaces() -> list:
    logging.debug('Detecting network interfaces.')
    try:
        response: str = popen('ifconfig').read()
        if not len(response):
            return []
        return response.split('\n\n')[:-1]
    except Exception as err:
        logging.warning(f'Warning getting network interfaces. {err}.')
    return []


@staticmethod
def get_access_points(interface: str) -> list:
    logging.debug(f'Detecting access points from interface "{interface}".')
    try:
        response: str = popen(f'sudo iwlist {interface} scan').read()
        if not len(response):
            return []
        return response.split('Cell')[1:]
    except Exception as err:
        logging.warning(f'Warning getting access points. {err}.')
    return []


@staticmethod
def get_connected_access_point(interface: str) -> str:
    logging.debug(f'Detecting connected access point from interface "{interface}".')
    try:
        response: str = popen(f'iwconfig {interface}').read()
        if not len(response):
            return ''
        return response.split('\n\n')[:-1][0]
    except Exception as err:
        logging.warning(f'Warning getting connected access point. {err}.')
    return ''
