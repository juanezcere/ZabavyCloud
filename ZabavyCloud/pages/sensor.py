import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..states.sensor import SensorState
from ..templates.single import SingleTemplate
from ..views.sensor import SensorView


@rx.page(
    route=Route.SENSOR.value,
    title=Title.SENSOR.value,
    description=Description.SENSOR.value,
    image=PREVIEW,
    meta=Metadata.SENSOR.value,
    # on_load=[SensorState.create_test_data],
)
def SensorPage() -> SingleTemplate:
    return SingleTemplate(
        title=Title.SENSOR.value,
        children=[
            SensorView(state=SensorState),
        ]
    )
