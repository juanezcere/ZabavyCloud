import reflex as rx

from ..components.card import CardList
from ..states.sensor import SensorState


def SensorView(state: SensorState):
    return rx.section(
        CardList(state=state),
        on_mount=state.get_data,
    )
