import reflex as rx

from .button import Button


class ConfirmState(rx.State):
    opened: bool = False

    @rx.event
    def show(self):
        self.opened = True

    @rx.event
    def close(self):
        self.opened = False


def Confirm(event: any, title: str = 'Delete register', description: str = 'Are you sure to delete this register?') -> rx.alert_dialog.root:
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.hstack(
                rx.vstack(
                    rx.alert_dialog.title(title),
                    rx.alert_dialog.description(description),
                ),
                Button(
                    image='x',
                    tooltip='Close',
                    event=ConfirmState.close,
                    color='red',
                ),
                justify='between',
            ),
            rx.center(
                Button(
                    image='trash',
                    tooltip='Delete',
                    event=event,
                    color='red',
                ),
                spacing='3',
                margin_y='16px',
            ),
        ),
        open=ConfirmState.opened,
    )
