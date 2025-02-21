import reflex as rx

from ..components.card import CardList
from ..states.variable import VariableState


def VariableView(state: VariableState):
    return rx.section(
        CardList(state=state),
        on_mount=state.get_data,
    )
