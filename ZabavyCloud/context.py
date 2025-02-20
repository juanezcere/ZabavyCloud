import ZabavyCloud.constants.app as const

from .app import App
from .begin import Begin
from .close import Close
from .loop import Loop
from .utils.logging_utils import configure_logging
from .utils.path_utils import join, mkdir
from .utils.time_utils import time


class Context:
    def __init__(self, begin: any = Begin(), loop: any = Loop(), close: any = Close()):
        self.const: any = const
        # self.ports: any = ports
        self.begin: any = begin
        self.loop: any = loop
        self.close: any = close
        data: dict = {
            'name': const.APP_NAME,
            'title': const.APP_TITLE,
            'icon': const.APP_ICON,
            'author': const.APP_AUTHOR,
            'version': const.APP_VERSION,
            'description': const.APP_DESCRIPTION,
            'summary': const.APP_SUMMARY,
            'host': const.HOST,
            'api_version': const.API_VERSION,
            'api_port': const.API_PORT,
            'web_version': const.WEB_VERSION,
            'web_port': const.WEB_PORT,
        }
        self.application: App = App(**data)
        self.application.paths = {
            name: join(path=[self.application.path, path]) for name, path in const.DATA_FOLDERS.items()
        }
        [mkdir(path=path) for path in self.application.paths.values()]
        logs_path = [self.application.paths['logs'], self.application.log_file]
        logs_file: str = join(path=logs_path)
        self.logging = configure_logging(name=self.application.name, file=logs_file,
                                         level=const.LOG_LEVEL)
        self.application.start: int = time()
        self.logging.info(f"Context '{self.application.name}' created.")

    def __enter__(self):
        """
        Enters to the application context.
        """
        self.logging.info(f"Starting the app '{self.application.name}'.")
        self.begin(context=self)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        Closing the application context.
        """
        self.logging.info(f"Closing the app '{self.application.name}'.")
        self.close(context=self)
