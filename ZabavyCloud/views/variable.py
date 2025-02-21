import reflex as rx

from ..components.card import CardList
from ..constants.route import Route
from ..states.variable import VariableState


def VariableView(state: VariableState):
    return rx.section(
        CardList(
            data=state.data,
            module=Route.VARIABLE.value
        ),
        on_mount=state.get_data,
    )
