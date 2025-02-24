import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..states.device import DeviceState
from ..templates.single import SingleTemplate
from ..views.device import DeviceView


@rx.page(
    route=Route.DEVICE.value,
    title=Title.DEVICE.value,
    description=Description.DEVICE.value,
    image=PREVIEW,
    meta=Metadata.DEVICE.value,
    # on_load=[DeviceState.create_test_data],
)
def DevicePage() -> SingleTemplate:
    return SingleTemplate(
        title=Title.DEVICE.value,
        children=[
            DeviceView(state=DeviceState),
        ]
    )
