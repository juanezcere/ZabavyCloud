import ZabavyCloud.repository as repository

from .pages.index import index as index_page
from .pages.variable import VariablePage as variable_page
from .routers.action import router as action_router
from .routers.actuator import router as actuator_router
from .routers.device import router as device_router
from .routers.gateway import router as gateway_router
from .routers.measure import router as measure_router
from .routers.sensor import router as sensor_router
from .routers.variable import router as variable_router


def build_repository(context: any) -> None:
    context.logging.debug("Building repository.")
    repository.create(repository='memory', name='database')
    context.repository = repository


def build_backend(context: any) -> None:
    context.logging.debug("Building backend.")
    context.app.api.title = context.application.title
    context.app.api.version = context.application.api_version
    context.app.api.description = context.application.description
    context.app.api.summary = context.application.summary
    context.app.api.contact = context.const.API_CONTACT
    context.app.api.license_info = context.const.LICENCE_INFO
    context.app.api.include_router(variable_router)
    context.app.api.include_router(action_router)
    context.app.api.include_router(sensor_router)
    context.app.api.include_router(actuator_router)
    context.app.api.include_router(device_router)
    context.app.api.include_router(gateway_router)
    context.app.api.include_router(measure_router)


def build_frontend(context: any) -> None:
    context.logging.debug("Building frontend.")
    context.app.add_page(index_page)
    context.app.add_page(variable_page)


class Begin:
    def __call__(self, context: any) -> None:
        context.logging.info(f"Beginning the software.")
        build_repository(context=context)
        build_backend(context=context)
        build_frontend(context=context)
        context.logging.info("Software successfully initialized.")
