import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..states.gateway import GatewayState
from ..templates.single import SingleTemplate
from ..views.gateway import GatewayView


@rx.page(
    route=Route.GATEWAY.value,
    title=Title.GATEWAY.value,
    description=Description.GATEWAY.value,
    image=PREVIEW,
    meta=Metadata.GATEWAY.value,
    # on_load=[GatewayState.create_test_data],
)
def GatewayPage() -> SingleTemplate:
    return SingleTemplate(
        title=Title.GATEWAY.value,
        children=[
            GatewayView(state=GatewayState),
        ]
    )
