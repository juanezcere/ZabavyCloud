import reflex as rx

from .button import Button
from .search import Search
from .form import Form


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
                    event=lambda: state.handle_delete(item.id),
                    color='red',
                ),
            ),
            align='center',
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
            Search(data=state.data),
            Button(
                image='plus',
                tooltip='Create',
                event=state.open_form,
                color='green',
            ),
            spacing='5',
            align='center',
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
                rx.dialog.title('Data creation'),
                rx.dialog.description('Form to create data.'),
                Form(state=state),
            ),
            open=state.opened,
        ),
        width='100%',
        spacing='3',
        align='center',
    )
