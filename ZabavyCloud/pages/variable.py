import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..states.variable import VariableState
from ..templates.single import SingleTemplate
from ..views.variable import VariableView


@rx.page(
    route=Route.VARIABLE.value,
    title=Title.VARIABLE.value,
    description=Description.VARIABLE.value,
    image=PREVIEW,
    meta=Metadata.VARIABLE.value,
    # on_load=[VariableState.create_test_data],
)
def VariablePage() -> SingleTemplate:
    return SingleTemplate(
        title=Title.VARIABLE.value,
        children=[
            VariableView(state=VariableState),
        ]
    )
