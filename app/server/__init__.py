"""
? Server
The server module is a class to configure FastAPI in the 'api' variable and a basic endpoint to validate the availability of the application.
"""
import logging

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import run

#from ..chess import game
from ..constants import app as const
from ..models.app import App


class Server:
    """
    ? This class configures FastAPI in the 'api' variable and a basic endpoint to validate the availability of the application.
    """

    api = FastAPI()

    def __init__(self, app: App):
        """
        ? Configures the API.
        params:
            ! app: App
                The App configuration.
        """
        logging.debug(f"Starting '{app.name}' server API.")
        self.host: str = app.host
        self.port: int = app.port
        self.api.title = app.title
        self.api.version = app.api_version
        self.api.description = app.description
        self.api.summary = app.summary
        self.api.contact = const.API_CONTACT
        self.api.license_info = const.LICENCE_INFO
        self.api.mount('/', StaticFiles(directory=app.paths['dist'], html=True), name='app')
        self.configure_cors()

    def register_route(self, router, prefix: str = '/', tags: list = []):
        """
        ? Registers a route on the API.
        params:
            ! router:
                The router to register to.
            * prefix: str = '/'
                The endpoint to mount the router.
            * tags: list = []
                The tags for the router.
        """
        logging.info(f"Registering router prefix '{prefix}' with tags '{tags}'.")
        self.api.include_router(router, prefix=prefix, tags=tags)

    def register_middleware(self, middleware, params: dict = {}):
        """
        ? Registers a middleware on the server.
        params:
            ! middleware: function
                The middleware to register.
            * params: dict
                A list of parameters to configure the middleware.
        """
        logging.info(f"Registering middleware '{middleware.__name__}'.")
        self.api.add_middleware(middleware, **params)

    def configure_cors(self, origins: list = const.ORIGINS):
        """
        ? Configures the CORS of the API.
        params:
            ! origins: list
                The origins to grant the permissions.
        """
        logging.debug(f"Adding CORS middleware to origins {origins}.")
        params = {
            'allow_origins': origins,
            'allow_credentials': True,
            'allow_methods': ['*'],
            'allow_headers': ['*']
        }
        self.register_middleware(middleware=CORSMiddleware, params=params)


    def serve(self) -> None:
        """
        Starts to serve the app.
        """
        logging.info(f"Starting the server on 'http://{self.host}:{self.port}'.")
        run(self.api, host=self.host, port=self.port, log_level='info')

    def close(self) -> None:
        """
        Closes the server.
        """
        pass


    # @api.on_event('startup')
    # async def startup():
    #     """
    #     ? Configures an event to connect to the database on startup.
    #     """
    #     await Database().database.connect()
# 
    # @api.on_event('shutdown')
    # async def shutdown():
    #     """
    #     ? Configures an event to disconnect to the database on shutdown.
    #     """
    #     await Database().database.disconnect()

    @api.get('/app', status_code=status.HTTP_200_OK)
    async def root_route(request: Request) -> dict:
        """
        ? Root endpoint to get availability of the API.
        params:
            ! request: Request
                The request information to the endpoint.
        """
        logging.debug(f'Requesting root route from "{request.client.host}".')
        return {
            'name': Server.api.title,
            'version': Server.api.version,
        }


    @api.get('/health', status_code=status.HTTP_200_OK)
    async def health_route(request: Request) -> str:
        """
        ? The status endpoint to get availability of the API.
        params:
            ! request: Request
                The request information to the endpoint.
        """
        logging.debug(f'Requesting health route from "{request.client.host}".')
        return 'OK'


    @api.get('/info', status_code=status.HTTP_200_OK)
    async def info_route(request: Request) -> dict:
        """
        ? Returns the detailed information of the API.
        params:
            ! request: Request
                The request information to the endpoint.
        """
        logging.debug(f'Requesting info route from "{request.client.host}".')
        return {
            'name': Server.api.title,
            'version': Server.api.version,
            'description': Server.api.description,
            'summary': Server.api.summary,
            'contact': Server.api.contact,
            'license': Server.api.license_info,
            'repository': const.REPOSITORY_URL,
        }


    @api.post('/run', status_code=status.HTTP_200_OK)
    async def app_route(request: Request, layout: int = 1) -> str:
        """
        ? Runs the application.
        params:
            ! request: Request
                The request information to the endpoint.
        """
        logging.debug(f'Requesting app route from "{request.client.host}".')
        if abs(layout) >= 2:
            return 'Err'
        try:
            game(layout=layout)
        except Exception as err:
            logging.error(f"Error executing app. {err}.")
        return 'OK'
