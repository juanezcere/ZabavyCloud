import reflex as rx

from .button import Button
from .confirm import Confirm, ConfirmState
from .form import Form
from .search import Search


def Card(state: any, item: any) -> rx.card:
    return rx.card(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.avatar(
                        rx.icon(tag=item.image, size=30),
                        fallback=item.name,
                        size='5',
                        radius='full',
                    ),
                    rx.separator(orientation='vertical'),
                    rx.box(
                        rx.heading(
                            item.name,
                            weight='bold',
                            size='7',
                            align='left',
                            trim='normal',
                        ),
                        rx.text(
                            item.description,
                            weight='light',
                            size='3',
                            align='left',
                            trim='normal',
                        ),
                        width='100%',
                    ),
                    rx.separator(orientation='vertical'),
                    spacing='3',
                    align='center',
                    justify='center',
                    width='100%',
                ),
                href=f'{state.module}/{item.id}',
            ),
            rx.hstack(
                Button(
                    image='pen',
                    tooltip='Edit',
                    event=lambda: state.handle_update(item.id),
                ),
                Button(
                    image='trash',
                    tooltip='Delete',
                    event=ConfirmState.show,
                    color='red',
                ),
                Confirm(
                    event=lambda: [
                        state.handle_delete(item.id),
                        ConfirmState.close()
                    ]
                ),
            ),
            align='center',
            justify='between',
        ),
        variant='surface',
        width='100%',
    )


def CardList(state: any) -> rx.vstack:
    return rx.vstack(
        rx.hstack(
            Button(
                image='refresh-cw',
                tooltip='Update',
                event=state.get_data,
            ),
            Search(event=state.handle_search),
            Button(
                image='plus',
                tooltip='Create',
                event=state.show_form,
                color='green',
            ),
            spacing='5',
            align='center',
            margin_y='16px',
        ),
        rx.data_list.root(
            rx.foreach(
                state.data,
                lambda item: rx.data_list.item(
                    Card(
                        state=state,
                        item=item,
                    ),
                    align='center',
                )
            ),
        ),
        rx.dialog.root(
            rx.dialog.content(
                Form(state=state),
            ),
            open=state.opened,
        ),
        width='100%',
        spacing='3',
        align='center',
    )
