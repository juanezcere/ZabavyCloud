import reflex as rx


def Button(image: str, tooltip: str, event: any, size: str = '2', radius: str = 'full', color: str = 'indigo', variant: str = 'classic', loading: bool = False, disabled: bool = False) -> rx.button:
    return rx.button(
        rx.tooltip(
            rx.icon(image),
            content=tooltip,
            side='bottom',
        ),
        # on_click=event,
        size=size,
        radius=radius,
        variant=variant,
        color_scheme=color,
        loading=loading,
        disabled=disabled,
        style={'cursor': 'pointer'},
    )
