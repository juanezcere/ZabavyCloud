import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..states.actuator import ActuatorState
from ..templates.single import SingleTemplate
from ..views.actuator import ActuatorView


@rx.page(
    route=Route.ACTUATOR.value,
    title=Title.ACTUATOR.value,
    description=Description.ACTUATOR.value,
    image=PREVIEW,
    meta=Metadata.ACTUATOR.value,
    # on_load=[ActuatorState.create_test_data],
)
def ActuatorPage() -> SingleTemplate:
    return SingleTemplate(
        title=Title.ACTUATOR.value,
        children=[
            ActuatorView(state=ActuatorState),
        ]
    )
