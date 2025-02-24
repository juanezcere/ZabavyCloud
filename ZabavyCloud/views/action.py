import reflex as rx

from ..components.card import CardList
from ..states.action import ActionState


def ActionView(state: ActionState):
    return rx.section(
        CardList(state=state),
        on_mount=state.get_data,
    )
