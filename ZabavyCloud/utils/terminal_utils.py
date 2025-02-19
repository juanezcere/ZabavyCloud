"""
Terminal utilities.
"""
from os import popen, system

from .decorator_utils import tryable
from .time_utils import sleep


@tryable
def reboot() -> None:
    """
    ? Reboots the operative system.
    """
    system('sudo reboot')


@tryable
def restart_usb() -> None:
    """
    ? Reboots the USB ports of the system.
    """
    system('sudo rmmod xhci_pci')
    sleep(duration=2)
    system('sudo modprobe xhci_pci')
    sleep(duration=1)


@tryable
def restart_network(interface: str) -> None:
    """
    ? Reboots the given network interface of the operative system.
    """
    system(f'sudo ifconfig {interface} down')
    sleep(duration=2)
    system(f'sudo ifconfig {interface} up')
    sleep(duration=1)


@tryable
def update_datetime() -> None:
    """
    ? Updates the date and time of the operative system from google.
    """
    system('sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d" " -f5-8)Z"')


@tryable
def get_network_interfaces() -> list:
    """
    ? Gets the network interfaces of the operative system.
    """
    response: str = popen('ifconfig').read()
    if not len(response):
        return []
    return response.split('\n\n')[:-1]


@tryable
def get_access_points(interface: str) -> list:
    """
    ? Gets the access points list from the given network inteface.
    """
    response: str = popen(f'sudo iwlist {interface} scan').read()
    if not len(response):
        return []
    return response.split('Cell')[1:]


@tryable
def get_connected_access_point(interface: str) -> str:
    """
    ? Returns the connected access point of the given network interface.
    """
    response: str = popen(f'iwconfig {interface}').read()
    if not len(response):
        return ''
    return response.split('\n\n')[:-1][0]
