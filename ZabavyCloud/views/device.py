import reflex as rx

from ..components.card import CardList
from ..states.device import DeviceState


def DeviceView(state: DeviceState):
    return rx.section(
        CardList(state=state),
        on_mount=state.get_data,
    )
