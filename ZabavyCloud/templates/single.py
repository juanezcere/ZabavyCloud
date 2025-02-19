import reflex as rx


def SingleTemplate(title: str, children: list) -> rx.container:
    return rx.container(
        rx.color_mode.button(position='top-right'),
        rx.heading(
            title,
            size='9',
            weight='bold',
            align='center',
            trim='normal',
        ),
        *children,
        rx.hstack(
            rx.logo(),
        ),
        size='4',
    )
