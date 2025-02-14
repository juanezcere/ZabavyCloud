"""
Logging Utilities.
"""
import logging

CONSOLE_FORMAT: str = '{asctime} [{levelname:^10}] ({process}) {name}: {message}'
FILE_FORMAT: str = '{asctime} [{levelname:^10}] ({process}) {pathname}=>{funcName}:{lineno}->{name}: {message}'
DATE_FORMAT: str = '%d/%m/%Y %H:%M:%S'


@staticmethod
def configure_logging(filename: str, level: int = logging.INFO) -> None:
    def add_console(logger):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter(CONSOLE_FORMAT, style='{', datefmt=DATE_FORMAT)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    def add_file(logger):
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FILE_FORMAT, style='{', datefmt=DATE_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    logger = logging.getLogger()
    logger.setLevel(level)
    add_console(logger=logger)
    add_file(logger=logger)
    #logging.root = logger
