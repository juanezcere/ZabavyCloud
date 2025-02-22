import reflex as rx


def Search(data: list) -> rx.input:
    return rx.input(
        rx.input.slot(
            rx.icon(tag='search'),
        ),
        placeholder='Search here...',
        radius='full',
        width='100%',
    ),
