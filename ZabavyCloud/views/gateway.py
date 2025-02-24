import reflex as rx

from ..components.card import CardList
from ..states.gateway import GatewayState


def GatewayView(state: GatewayState):
    return rx.section(
        CardList(state=state),
        on_mount=state.get_data,
    )
