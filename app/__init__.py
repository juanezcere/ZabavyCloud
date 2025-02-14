import logging

#from .chess import game
from .constants import app as const
from .models.app import App
from .server import Server
from .utils.configure_logging import configure_logging
from .utils.path_utils import create_directory, join_directory
from .utils.time_utils import duration_time, time

__name__: str = 'Zabavy'
__version__: str = '1.0.0'


class Zabavy:

    def __init__(self):
        data: dict = {
            'name': const.NAME,
            'title': const.TITLE,
            'icon': const.ICON,
            'version': const.VERSION,
            'author': const.AUTHOR,
            'api_version': const.API_VERSION,
            'web_version': const.WEB_VERSION,
            'description': const.DESCRIPTION,
            'summary': const.SUMMARY,
            'host': const.HOST,
            'port': const.PORT,
        }
        self.app: App = App(**data)
        self.app.paths: dict = {
            'data': join_directory([self.app.path, 'data']),
            'dist': join_directory([self.app.path, 'dist']),
            'assets': join_directory([self.app.path, 'assets']),
            'logs': join_directory([self.app.path, 'data', 'logs']),
            'temp': join_directory([self.app.path, 'data', 'temp']),
            'saved': join_directory([self.app.path, 'data', 'saved']),
            'uploads': join_directory([self.app.path, 'data', 'uploads']),
        }
        [create_directory(path=path) for path in self.app.paths.values()]
        logs_file: str = join_directory([self.app.paths['logs'], self.app.log_file])
        configure_logging(name=const.NAME, filename=logs_file, level=const.LOG_LEVEL)

    def __enter__(self):
        """
        Enters to the application context.
        """
        logging.info(f"Starting '{self.app.name}' application.")
        logging.debug(f"Application version: {self.app.version}.")
        logging.debug(f"Application path: '{self.app.path}'.")
        logging.debug(f"Platform: '{self.app.system} {self.app.release}'.")
        self.server: Server = Server(app=self.app)
        self.app.start: int = time()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        logging.info(f"Closing app '{self.app.name}'.")
        self.server.close()
        duration: float = duration_time(self.app.start)
        logging.debug(f"Execution time: {duration} s.")

    def run(self) -> None:
        self.server.serve()

    #def start(self) -> None:
    #    game()
