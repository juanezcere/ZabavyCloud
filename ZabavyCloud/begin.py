from .pages.index import index as index_page
from .routers.action import router as action_router
from .routers.actuator import router as actuator_router
from .routers.device import router as device_router
from .routers.gateway import router as gateway_router
from .routers.measure import router as measure_router
from .routers.sensor import router as sensor_router
from .routers.variable import router as variable_router


def build_backend(context: any) -> None:
    context.logging.debug("Building backend.")
    context._app.api.title = context.app.title
    context._app.api.version = context.app.api_version
    context._app.api.description = context.app.description
    context._app.api.summary = context.app.summary
    context._app.api.contact = context.const.API_CONTACT
    context._app.api.license_info = context.const.LICENCE_INFO
    context._app.api.include_router(variable_router)
    context._app.api.include_router(action_router)
    context._app.api.include_router(sensor_router)
    context._app.api.include_router(actuator_router)
    context._app.api.include_router(device_router)
    context._app.api.include_router(gateway_router)
    context._app.api.include_router(measure_router)


def build_frontend(context: any) -> None:
    context.logging.debug("Building frontend.")
    context._app.add_page(index_page)


class Begin:
    def __call__(self, context: any) -> None:
        context.logging.info(f"Beginning the software.")
        build_backend(context=context)
        build_frontend(context=context)
        context.logging.info("Software successfully initialized.")
