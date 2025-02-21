import reflex as rx

from rxconfig import config

from ..constants.meta import PREVIEW, Description, Metadata, Title
from ..constants.route import Route
from ..templates.single import SingleTemplate


class State(rx.State):
    """The app state."""
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


@rx.page(
    route=Route.INDEX.value,
    title=Title.INDEX.value,
    description=Description.INDEX.value,
    image=PREVIEW,
    meta=Metadata.INDEX.value,
)
def index() -> SingleTemplate:
    return SingleTemplate(
        title='Index',
        children=[
            rx.center(
                rx.button(
                    "Decrement",
                    color_scheme="ruby",
                    on_click=State.decrement,
                ),
                rx.heading(State.count, font_size="2em"),
                rx.button(
                    "Increment",
                    color_scheme="grass",
                    on_click=State.increment,
                ),
                spacing="4",
                style={'padding': '5px'}
            )
        ]
    )
