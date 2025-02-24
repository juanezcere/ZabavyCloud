import reflex as rx


def Search(event: any) -> rx.input:
    return rx.input(
        rx.input.slot(
            rx.icon(tag='search'),
        ),
        on_change=event,
        placeholder='Search here...',
        radius='full',
        width='100%',
    )
