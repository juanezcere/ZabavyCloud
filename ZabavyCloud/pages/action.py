import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..states.action import ActionState
from ..templates.single import SingleTemplate
from ..views.action import ActionView


@rx.page(
    route=Route.ACTION.value,
    title=Title.ACTION.value,
    description=Description.ACTION.value,
    image=PREVIEW,
    meta=Metadata.ACTION.value,
    # on_load=[ActionState.create_test_data],
)
def ActionPage() -> SingleTemplate:
    return SingleTemplate(
        title=Title.ACTION.value,
        children=[
            ActionView(state=ActionState),
        ]
    )
