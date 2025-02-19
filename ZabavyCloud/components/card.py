import reflex as rx


def Card():
    return rx.card(
        rx.link(
            rx.flex(
                rx.avatar(src="/reflex_banner.png"),
                rx.box(
                    rx.heading("Quick Start"),
                    rx.text(
                        "Get started with Reflex in 5 minutes."
                    ),
                ),
                spacing="2",
            ),
        ),
        as_child=True,
    )
