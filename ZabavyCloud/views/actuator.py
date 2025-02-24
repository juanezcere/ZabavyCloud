import reflex as rx

from ..components.card import CardList
from ..states.actuator import ActuatorState


def ActuatorView(state: ActuatorState):
    return rx.section(
        CardList(state=state),
        on_mount=state.get_data,
    )
